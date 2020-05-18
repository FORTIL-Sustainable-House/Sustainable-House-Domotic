from flask_wtf import FlaskForm

from app.dummy_feature.models import Room
from wtforms import FloatField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

# Form to add a new room.
class RoomForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	area = FloatField('Area')
	submit = SubmitField('Add')
