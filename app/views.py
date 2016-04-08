from flask import (Blueprint, render_template, g, redirect,
                   url_for, request, flash, jsonify)
from flask.ext.login import login_user, logout_user, login_required
from flask_login import current_user

from app import login_manager
from person.person import EmployeeController
from person.forms import LoginForm

init = Blueprint('init', __name__)


@login_manager.user_loader
def load_user(userid):
    return EmployeeController.get_by_id(userid)


@init.route('/')
def index():
    if current_user.is_anonymous:
        login_form = LoginForm()
        return render_template(
            "defaults/login.html",
            title="Login",
            login_form=login_form
        )
    else:
        return redirect(url_for('init.dashboard'))


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
                msg = None
                url = url_for('init.dashboard')
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


@init.route('/dashboard/')
@login_required
def dashboard():
    return render_template(
        'defaults/dashboard.html',
        title="Dashboard"
    )


@init.route('/dashboard/settings')
def settings():
    return render_template(
        'defaults/settings.html',
        title="Settings"
    )
