from flask_wtf import Form
from wtforms import DateTimeField, StringField
from wtforms.validators import DataRequired, Length


class SingInVisitorForm(Form):
    visitor_id = StringField(
        label="Visitor ID",
        validators=[
            DataRequired(),
            Length(max=15)
        ]
    )

    first_name = StringField(
        label="First Name",
        validators=[
            DataRequired(),
        ]
    )

    last_name = StringField(
        label="Last Name",
        validators=[
            DataRequired(),
        ]
    )

    street_name = StringField(
        label="Street Name",
        validators=[
            DataRequired()
        ]
    )

    city_state = StringField(
        label="City & State",
        validators=[
            DataRequired()
        ]
    )

    date_of_birth = DateTimeField(
        label="Date of Birth",
        validators=[
            DataRequired()
        ]
    )

    host_id = StringField(
        label="Student ID",
        validators=[
            DataRequired()
        ]
    )

    host_room = StringField(
        label="Host Room #",
        validators=[
            DataRequired()
        ]
    )
