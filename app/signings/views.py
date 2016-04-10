from flask import (Blueprint, render_template, g, redirect,
                   url_for, request, flash, jsonify)
from flask.ext.login import login_required

from .forms import SingInVisitorForm
from .signings import SigningsController

from app.person.person import StudentController

signings = Blueprint("signings", __name__)


@signings.route('/dashboard/sign-in-visitor')
@login_required
def signin_visitor():
    student = StudentController.get_student_by_student_id("01554763")
    SigningsController.create_signing("ICC", student, "what", "test")

    return render_template(
        'person/signing_visitor.html',
        title="Sign-In Visitor",
        form=SingInVisitorForm()
    )
