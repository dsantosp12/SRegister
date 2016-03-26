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
        pass


class HostRoomFull(Exception):
    pass


class VisitorNoInSystem(Exception):
    pass


class VisitorLiveHere(Exception):
    pass
