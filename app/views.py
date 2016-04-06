from flask import (Blueprint, render_template, g, redirect,
                   url_for, request, flash, jsonify)
from flask.ext.login import login_user, logout_user

from app import login_manager
from person.person import EmployeeController
from person.forms import LoginForm

init = Blueprint('init', __name__)


@login_manager.user_loader
def load_user(userid):
    return EmployeeController.get_by_id(userid)


@init.route('/')
def index():
    login_form = LoginForm()
    return render_template(
        "defaults/login.html",
        title="Login",
        login_form=login_form
    )


@init.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    status = "error"
    msg = "Username or password doesn't match"
    url = None

    if form.is_submitted():
        username = form.username.data
        password = form.password.data
        try:
            employee = EmployeeController.get_by_username(username)
        except EmployeeController.EmployeeDoesNotExist:
            pass
        else:
            if EmployeeController.validate_user(username, password):
                login_user(employee)
                status = "success"
                msg = "Welcome back " + employee.first_name
                url = url_for('signings.dashboard')
        return jsonify(
            status=status,
            msg=msg,
            url=url
        )
    else:
        return redirect(url_for('init.index'))


@init.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('init.index'))
