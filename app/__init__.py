from flask import Flask, render_template, g
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
# TODO: Install mail library
# from flask.ext.mail import Mail
import flask_login

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

# LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'init.index'


@app.before_request
def before_request():
    g.user = flask_login.current_user
    g.domain = "http://0.0.0.0:5000"


# HTTP error handlers
@app.errorhandler(400)
def page_not_found(error):
    # TODO: Add 404 html
    return "404 Error"


# Default views
from app.views import init
app.register_blueprint(init)

from app.signings.views import signings
app.register_blueprint(signings)

# Student, Person and Employee views
from app.person.views import person
app.register_blueprint(person)

# Building views
from app.building.views import buildings

# Setup
if __name__ == 'app':
    db.create_all()
