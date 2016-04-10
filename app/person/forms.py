from flask_wtf import Form
from wtforms import StringField, PasswordField, DateTimeField, RadioField
from wtforms.validators import DataRequired, Length, Regexp


class LoginForm(Form):
    username = StringField(
        label="Username",
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        label="Password",
        validators=[
            DataRequired()
        ]
    )
