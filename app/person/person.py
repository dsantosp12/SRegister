from app.person.model import *


class StudentController:
    def __init__(self, student_id):
        self.student_id = student_id

    def create(self):
        pass

    @staticmethod
    def create_student(first_name, last_name,
                       student_id):
        pass

    @staticmethod
    def get_student_by_student_id(student_id):
        pass

    @staticmethod
    def get_student_by_id(pk):
        pass

    @staticmethod
    def exist(student_id):
        pass

    @staticmethod
    def delete_student(student_id):
        pass

    @staticmethod
    def modify_first_name(student_id, new_first_name):
        pass

    @staticmethod
    def modify_last_name(student_id, new_last_name):
        pass

    @staticmethod
    def modify_student_id(old_id, new_id):
        pass


class VisitorController:

    def __init__(self, visitor):
        self.visitor = visitor

    @staticmethod
    def get_visitor_by_visitor_id(visitor_id):
        pass
