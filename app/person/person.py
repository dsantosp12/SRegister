from flask.ext.bcrypt import check_password_hash, generate_password_hash

from app.person.model import Student, Employee, Visitor
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
        new_student = Student(first_name, last_name, student_id)
        db.session.add(new_student)
        db.session.commit()

    @staticmethod
    def create_student_object(student):
        pass

    @staticmethod
    def get_student_by_student_id(student_id):
        return Student.query.filter_by(
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
        student = StudentController.get_student_by_student_id(student_id)
        db.session.delete(student)
        db.session.commit()

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
    def create_visitor(first_name, last_name,
                       visitor_id, date_of_birth,
                       address):
        db.session.add(
            Visitor(
                first_name, last_name,
                visitor_id, date_of_birth,
                address
            )
        )
        db.session.commit()

    @staticmethod
    def create_visitor_object(visitor):
        db.session.add(
            Visitor(
                visitor.first_name,
                visitor.last_name,
                visitor.visitor_id,
                visitor.date_of_birth,
                visitor.address
            )
        )
        db.session.commit()

    @staticmethod
    def get_visitor_by_visitor_id(visitor_id):
        visitor = Visitor.query.filter_by(visitor_id=visitor_id).first()
        if visitor:
            return visitor
        else:
            raise VisitorNoInSystem("This visitor is no in the system")


class VisitorNoInSystem(Exception):
    pass


class EmployeeController(object):

    @staticmethod
    def create_employee(first_name, last_name,
                        employee_id, username,
                        password, email):
        db.session.add(
            Employee(
                first_name, last_name,
                employee_id, username,
                EmployeeController._hash_password(
                    password
                ),
                email
            )
        )
        db.session.commit()

    @staticmethod
    def get_by_username(username):
        employee = Employee.query.filter_by(
            username=username
        ).first()
        if employee:
            return employee
        else:
            raise EmployeeController.EmployeeDoesNotExist

    @staticmethod
    def get_by_id(userid):
        employee = Employee.query.filter_by(
            id=userid
        ).first()
        if employee:
            return employee
        else:
            raise EmployeeController.EmployeeDoesNotExist

    @staticmethod
    def validate_user(username, password):
        username = EmployeeController.get_by_username(username)

        return EmployeeController._verify_hash(
            username.password, password
        )


    @staticmethod
    def _verify_hash(original, hash):
        return check_password_hash(original, hash)

    @staticmethod
    def _hash_password(password):
        return generate_password_hash(password)

    class EmployeeDoesNotExist(Exception):
        pass
