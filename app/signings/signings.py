import datetime

from app import db
from .model import Signing, Session


class SigningsController:

    def __init__(self, signing):
        self.signing = signing

    @staticmethod
    def get_signing_by_id(pk_id):
        pass

    @staticmethod
    def create_signing_object(signing):
        pass

    @staticmethod
    def create_signing(building, host, visitor, employee):
        print(SigningsController._get_today_signings_by_host(host))

    # TODO:DS Need to be tested
    @staticmethod
    def _get_today_signings_by_host(host):
        """Returns a list of today signings by the given host."""
        session = SigningsController.get_session_limits()
        lower_limit = session.lower_limit

        upper_limit = session.upper_limit

        return db.session.query(Signing).filter(
            Signing.host == host.student_id,
            Signing.date_time >= lower_limit,
            Signing.date_time < upper_limit
        ).all()

    @staticmethod
    def get_session_limits():
        return Session.query.filter_by(id=1).first()


class HostRoomFull(Exception):
    pass


class VisitorNoInSystem(Exception):
    pass


class VisitorLiveHere(Exception):
    pass
