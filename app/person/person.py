from app.person.model import Student
from app import db


class StudentController:
    def __init__(self, first_name, last_name, student_id):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def create(self):
        new_student = Student(
            self.first_name,
            self.last_name,
            self.student_id
        )
        db.session.add(new_student)
        db.session.commit()

    @staticmethod
    def create_student(first_name, last_name,
                       student_id):
        pass

    @staticmethod
    def create_student_object(student):
        pass

    @staticmethod
    def get_student_by_student_id(student_id):
        return Student.query.filter(
            student_id=student_id
        ).first()

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


class EmployeeController(object):
    pass
