from wtforms import Form, DateTimeField, StringField
from wtforms.validators import DataRequired, Length

class SingInVisitorForm(Form):
    visitor_id = StringField(
        label="Visitor ID",
        validators=[
            DataRequired(),
            Length(max=15)
        ]
    )

    visitor_name = StringField(
        label="Visitor Name",
        validators=[
            DataRequired(),
        ]
    )

    street_name = StringField(
        label="Stree Name",
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
