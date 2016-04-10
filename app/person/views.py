from flask import Blueprint, render_template
from .person import StudentController

person = Blueprint('person', __name__)
