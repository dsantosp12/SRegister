from flask import Blueprint
from .person import StudentController

person = Blueprint('person', __name__)
