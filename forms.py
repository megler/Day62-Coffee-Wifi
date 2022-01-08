from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import URL, DataRequired


class CafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name", validators=[DataRequired()])
    cafe_location = StringField(
        label="Cafe Location On Google Maps (URL)",
        validators=[DataRequired(), URL(message="Must enter URL")],
    )
    cafe_open = StringField(
        label="Opening Time e.g. 8AM", validators=[DataRequired()]
    )
    cafe_close = StringField(
        label="Closing Time e.g. 5:30PM", validators=[DataRequired()]
    )
    coffee_rating = SelectField(
        label="Coffee Rating",
        validators=[DataRequired()],
        choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
    )
    wifi_strength = SelectField(
        label="Wifi Strength Rating",
        validators=[DataRequired()],
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
    )
    power_avail = SelectField(
        label="Power Socket Availability",
        validators=[DataRequired()],
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
    )
    submit = SubmitField(label="Submit")
