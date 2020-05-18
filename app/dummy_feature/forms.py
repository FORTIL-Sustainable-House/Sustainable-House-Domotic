from flask_wtf import FlaskForm

from app.dummy_feature.models import Environment, Room
from wtforms import FloatField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

# Form to add a new environment.
class EnvironmentForm(FlaskForm):
    label = StringField('Label', validators=[DataRequired()])
    submit = SubmitField('Add')

# Form to add a new room.
class RoomForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	area = FloatField('Area')
	environments = SelectField('Choose an environment', coerce=int)
	submit = SubmitField('Add')
