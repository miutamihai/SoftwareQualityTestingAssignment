from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    date_of_birth = DateField('date_of_birth', validators=[DataRequired()])
    vehicle_value = IntegerField('vehicle_value', validators=[DataRequired()])
    penalty_points = IntegerField('penalty_points', validators=[DataRequired()])
    cover_type = SelectField('cover_type', validators=[DataRequired()])
    submit = SubmitField('submit')