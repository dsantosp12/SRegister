from flask import Blueprint, render_template
from .person import StudentController
from .forms import SingInVisitorForm

person = Blueprint('person', __name__)


@person.route('/dashboard/sign-in-visitor')
def signin_visitor():
    return render_template(
        'person/signing_visitor.html',
        title="Sign-In Visitor",
        form=SingInVisitorForm()
    )
