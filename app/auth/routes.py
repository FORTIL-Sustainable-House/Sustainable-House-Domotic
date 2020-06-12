from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User


# Login page route
@bp.route('/login', methods=['GET', 'POST'])
def login():
	# If already authenticated, redirect to the index
	if current_user.is_authenticated:
		return redirect(url_for('management.dashboard'))
	# Get the login Form
	form = LoginForm()
	# When form is filled, get user and password and see if they exist
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		# Redirect to login with an error if incorrect user or password
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('auth.login'))
		# Login the user and redirect to the target page or the index
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('management.dashboard')
		return redirect(next_page)
	# Render login page with form to fill
	return render_template('auth/login.html', title='Sign In', form=form)


# Logout page, redirect to login page
@bp.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('auth.login'))


# Register page
@bp.route('/register', methods=['GET', 'POST'])
def register():
	# Redirect to the index if already authetified
	if current_user.is_authenticated:
		return redirect(url_for('management.dashboard'))
	# If the registration form is filled by the user, create user and redirect to login page
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('auth.login'))
	# Render the registration page with form to fill
	return render_template('auth/register.html', title='Register', form=form)


# Index home page
@bp.route('/')
@bp.route('/index')
@login_required
def index():
	if current_user.is_authenticated:
		user = current_user.username
	else:
		user = 'anonymous'
	return render_template('auth/index.html', title='SusHouse_v0.0.1', user=user)