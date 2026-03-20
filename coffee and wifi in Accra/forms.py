from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_url = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    opening_time = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        validators=[DataRequired()],
        choices=[
            ("☕️", "☕️"),
            ("☕️☕️", "☕️☕️"),
            ("☕️☕️☕️", "☕️☕️☕️"),
            ("☕️☕️☕️☕️", "☕️☕️☕️☕️"),
            ("☕️☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"),
        ],
    )
    wifi_strength = SelectField(
        "Wifi Strength Rating",
        validators=[DataRequired()],
        choices=[
            ("✘", "✘"),
            ("💪", "💪"),
            ("💪💪", "💪💪"),
            ("💪💪💪", "💪💪💪"),
            ("💪💪💪💪", "💪💪💪💪"),
            ("💪💪💪💪💪", "💪💪💪💪💪"),
        ],
    )
    power_outlet = SelectField(
        "Power Socket Availability",
        validators=[DataRequired()],
        choices=[
            ("✘", "✘"),
            ("🔌", "🔌"),
            ("🔌🔌", "🔌🔌"),
            ("🔌🔌🔌", "🔌🔌🔌"),
            ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"),
        ],
    )
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
