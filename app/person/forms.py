from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, Email


class LoginForm(Form):
    username = StringField(

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
