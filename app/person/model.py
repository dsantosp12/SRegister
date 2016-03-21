import datetime

from app import db
from flask_login import UserMixin


class Person(UserMixin, db.Model):
    """Person model"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<Person: %r %r>" % (self.first_name,
                                    self.last_name)


class Student(Person):
    student_id = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def __repr__(self):
        return "<Student: %r %r>" % (self.first_name,
                                    self.last_name)


class Visitor(Person):
    visitor_id = db.Column(db.String(255), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name, visitor_id,
                 date_of_birth, address):
        super().__init__(first_name, last_name)
        self.visitor_id = visitor_id
        self.date_of_birth = date_of_birth
        self.address = address

    def __repr__(self):
        return "<Visitor: %r %r>" % (self.first_name,
                                    self.last_name)


class Employee(Person):
    employee_id = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, first_name, last_name, employee_id, username,
                 password, email):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<Employee: %r %r>" % (self.first_name, self.last_name)
