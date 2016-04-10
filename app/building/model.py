from app import db


class Building(db.Model):
    """Building model"""
    id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, building_name):
        self.building_name = building_name

    def __repr__(self):
        return "<Building: %r>" % self.building_name
