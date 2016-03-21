import datetime

from app import db


class Signing(db.Model):
    """Signing model"""
    id = db.Column(db.Integer, primary_key=True)
    # TODO: Solve problem with default date_time
    date_time = db.Column(db.DateTime, default=datetime.datetime.now)
    building = db.Column(db.String(255), db.ForeignKey('building.building_name'))
    host = db.Column(db.String(255), db.ForeignKey('student.student_id'))
    visitor = db.Column(db.String(255), db.ForeignKey('person.id'))
    employee = db.Column(db.String(255), db.ForeignKey('employee.employee_id'))

    def __init__(self, building, host, visitor, employee):
        self.building = building
        self.host = host
        self.visitor = visitor
        self.employee = employee

    def __repr__(self):
        return "<Signing: %r %r %r>" % (self.host, self.visitor,
                                        self.date_time_to_string())

    def date_time_to_string(self):
        return self.date_time.strftime("%m/%d/%y - %I:%M %p")
