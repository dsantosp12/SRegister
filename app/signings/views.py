from flask import (Blueprint, render_template, redirect,
                   url_for, request, jsonify)
from flask.ext.login import login_required
import flask_login

from app.person.model import Visitor, Student
from .forms import SingInVisitorForm
from .controller import SigningsController
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
        try:
            SigningsController.create_signing(
                "ICC",
                form.host_id.data,
                Visitor(form=form),
                flask_login.current_user
            )
        except SigningsController.HostRoomFull as e:
            status = "error"
            msg = str(e)
        else:
            status = "success"
            msg = "Sign In Created Successfully"

        return jsonify(
            status=status,
            msg=msg
        )

    return render_template(
        'person/signing_visitor.html',
        title="Sign-In Visitor",
        form=form
    )
