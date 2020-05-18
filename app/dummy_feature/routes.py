from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.dummy_feature import bp
from app.dummy_feature.forms import EnvironmentForm, RoomForm
from app.dummy_feature.models import Environment, Room

# Main page.
@bp.route('/dummy_page')
@login_required
def dummy_page():
    # Retrieve environments.
    environments = Environment.query.all()
    rooms = Room.query.all()

    # Render the page
    return render_template(
        'dummy_feature/dummy_page.html', 
        title='Dummy Title', 
        environments=environments,
        rooms=rooms
    )

# Method to add an environment.
@bp.route('/environment/add', methods=['GET', 'POST'])
@login_required
def add_environment():
    # If user is not authenticated, redirect to login page.
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    
    form = EnvironmentForm()
    
    # If form is correctly filled, add in database.
    # Redirect to main page.
    if form.validate_on_submit():
        environment = Environment(label=form.label.data)
        db.session.add(environment)
        db.session.commit()
        flash('Congratulations, you added a new environment!')
        return redirect(url_for('dummy_feature.dummy_page'))
    
    # Redirect to form to add environment.
    return render_template('dummy_feature/add_environment.html', title='Add environment', form=form)    

# Method to add a room.
@bp.route('/room/add', methods=['GET', 'POST'])
@login_required
def add_room():
    # If user is not authenticated, redirect to login page.
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    form = RoomForm()

    # Retrieve all environments to fill dropdown list.
    environments = Environment.query.order_by('label')
    form.environments.choices = [(e.id, e.label) for e in environments]

    # If form is correctly filled, add in database.
    # Redirect to main page.
    if form.validate_on_submit():
        room = Room(
            name=form.name.data, 
            area=form.area.data, 
            environment_id=form.environments.data
        )
        db.session.add(room)
        db.session.commit()
        flash('Congratulations, you added a new room!')
        return redirect(url_for('dummy_feature.dummy_page'))

    # Redirect to form to add room.
    return render_template('dummy_feature/add_room.html', title='Add room', form=form)
