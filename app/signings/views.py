from flask import (Blueprint, render_template, redirect,
                   url_for, request, jsonify)
from flask.ext.login import login_required
import flask_login

from app.person.model import Visitor
from .forms import SingInVisitorForm
from .signings import SigningsController
from app.person.person import StudentController, EmployeeController

signings = Blueprint("signings", __name__)  


def update_session():
    SigningsController.update_session()


@signings.before_request
def before_request():
    update_session()


@signings.route('/dashboard/sign-in-visitor', methods=['GET', 'POST'])
@login_required
def signin_visitor():
    form = SingInVisitorForm()
    status = "error"
    msg = "We couldn't sign-in this visitor"

    if form.is_submitted():
        current_employee = flask_login.current_user

        # visitor = Visitor(form.visitor_name.data)


    return render_template(
        'person/signing_visitor.html',
        title="Sign-In Visitor",
        status=status,
        msg=msg,
        form=form
    )
