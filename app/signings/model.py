import datetime

from app import db


class Signing(db.Model):
    """Signing model"""
    id = db.Column(db.Integer, primary_key=True)
    # TODO: Solve problem with default date_time
    date_time = db.Column(db.DateTime)
    building = db.Column(db.String(255), db.ForeignKey('building.building_name'))
    host = db.Column(db.String(255), db.ForeignKey('student.student_id'))
    visitor = db.Column(db.String(255), db.ForeignKey('visitor.visitor_id'))
    employee = db.Column(db.String(255), db.ForeignKey('employee.employee_id'))

    def __init__(self, building, host, visitor, employee):
        self.date_time = datetime.datetime.now
        self.building = building.building_name
        self.host = host.student_id
        self.visitor = visitor.id
        self.employee = employee.employee_id

    def __repr__(self):
        return "<Signing: %r %r %r>" % (self.host, self.visitor,
                                        self.date_time_to_string())

    def date_time_to_string(self):
        return self.date_time.strftime("%m/%d/%y - %I:%M %p")


class Session(db.Model):
    """This model is use to quick track of the current session"""
    id = db.Column(db.Integer, primary_key=True)
    upper_limit = db.Column(db.DateTime)
    lower_limit = db.Column(db.DateTime)

    def __init__(self, upperl, lowerl):
        self.upper_limit = upperl
        self.lower_limit = lowerl

    def __repr__(self):
        return "<Session: %r>" % self.limits_to_string()

    def limits_to_string(self):
        return "Lower: %r Upper %r" % (
            self.lower_limit.strftime("%m/%d/%y - %I:%M %p"),
            self.upper_limit.strftime("%m/%d/%y - %I:%M %p")
        )
