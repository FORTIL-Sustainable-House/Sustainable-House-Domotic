from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app.auth.models import User


# Registration form to create a ew user
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


# Login form for connection
class LoginForm(FlaskForm):
    username_style={'class':'form-control', 'placeholder':'Username'}
    password_style={'class':'form-control', 'placeholder':'Password'}
    remember_me_style={'class':'custom-control-input'}
    submit_style={'class':'btn form-btn'}

    username = StringField('Username', validators=[DataRequired()], render_kw=username_style)
    password = PasswordField('Password', validators=[DataRequired()], render_kw=password_style)
    remember_me = BooleanField('Remember Me', render_kw=remember_me_style)
    submit = SubmitField('Sign in', render_kw=submit_style)
