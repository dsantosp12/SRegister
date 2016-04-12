import datetime
from sqlalchemy import sql

from app import db
from .model import Signing, Session
from person.person import VisitorController, VisitorNoInSystem


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
    def create_signing(building_name, host, visitor, employee):
        if SigningsController._get_today_signings_by_host(host).__len__() == 2:
            raise HostRoomFull("{} already has two visitor.".format(host.first_name))
        else:
            try:
                VisitorController.get_visitor_by_visitor_id(visitor.visitor_id)
            except VisitorNoInSystem:
                VisitorController.create_visitor_object(visitor)
            finally:
                db.session.add(
                    Signing(
                        building_name,
                        host,
                        visitor,
                        employee
                    )
                )
                db.session.commit()

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

    @staticmethod
    def update_session():
        now = datetime.datetime.now()
        if 17 <= now.hour <= 23:
            lower_limit = datetime.datetime(
                datetime.datetime.today().year,
                datetime.datetime.today().month,
                datetime.datetime.today().day,
                19
            )
            upper_limit = datetime.datetime(
                datetime.datetime.today().year,
                datetime.datetime.today().month,
                datetime.datetime.today().day + 1,
                7
            )

            db.session.execute(
                sql.update(Session).where(
                    Session.id == 1
                ).values(
                    upper_limit=upper_limit,
                    lower_limit=lower_limit
                )
            )
            db.session.commit()


class HostRoomFull(Exception):
    pass


class VisitorLiveHere(Exception):
    pass
