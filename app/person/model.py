import datetime

from app import db
from flask_login import UserMixin


class Person():
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(db.Model, Person):
    student_id = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, first_name=None, last_name=None, student_id=None, form=None):
        Person.__init__(self, first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __repr__(self):
        return "<Student: %r %r>" % (self.first_name, self.last_name)


class Visitor(db.Model, Person):
    visitor_id = db.Column(db.String(255), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name=None, last_name=None, visitor_id=None,
                 date_of_birth=None, address=None, form=None):
        if form:
            Person.__init__(self, form.first_name.data, form.last_name.data)
            self.visitor_id = form.visitor_id.data
            self.date_of_birth = form.date_of_birth.data
            self.address = "{} {}".format(form.street_name.data, form.city_state.data)
        else:
            Person.__init__(self, last_name, last_name)
            self.visitor_id = visitor_id
            self.date_of_birth = date_of_birth
            self.address = address

    def __repr__(self):
        return "<Visitor: %r %r>" % (self.first_name, self.last_name)


class Employee(UserMixin, db.Model, Person):
    employee_id = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, first_name, last_name, employee_id, username,
                 password, email):
        Person.__init__(self, first_name, last_name)
        self.employee_id = employee_id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<Employee: %r %r>" % (self.first_name, self.last_name)
