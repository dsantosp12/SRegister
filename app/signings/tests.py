import unittest
import datetime

from app.person.model import *
from app.signings.model import *
from app.building.model import *
from app.person.person import *
from app.building.building import *
from app.signings.signings import *


class TestSigningController(unittest.TestCase):

    def setUp(self):
        self.building = Building("Fox Hall")
        BuildingController.create_building_object(self.building)
        self.student = Student("Will", "Pat", "Z0000000", "Fox Hall")
        StudentController.create_student_object(self.student)
        self.visitor = Visitor(
            "John", "Smith",
            "Z9999999", datetime.date(2016, 2, 22),
            "123 Main St Lowell, MA 01843"
        )
        VisitorController.create_visitor_object(self.visitor)
        self.employee = Employee(
            "Daniel", "Santos", "E2222222",
            "dsantos", "Mysecurepass",
            "daniel_santos@student.uml.edu"
        )
        EmployeeController.create_employee_object(self.employee)
        self.signing = Signing(
            self.building,
            self.student,
            self.visitor,
            self.employee
        )
        self.signing_controller = SigningsController(
            self.signing
        )

    def tearDown(self):
        BuildingController.delete_building(self.building.id)
        StudentController.delete_student(self.student.student_id)
        VisitorController.delete_visitor(self.visitor.visitor_id)
        EmployeeController.delete_employee(self.employee.employee_id)
        SigningsController.delete_signing(self.signing.id)

    def test_create_signing_method(self):
        self.signing_controller.create()

        self.assertIsNotNone(
            SigningsController.get_signing_by_id(
                pk_id=self.signing.id
            )
        )

    def test_create_signing_static_method(self):
        SigningsController.create_signing(
            building=self.building,
            host=self.student,
            visitor=self.visitor,
            employee=self.employee
        )

        self.assertIsNotNone(
            SigningsController.get_signing_by_id(
                self.signing.id
            )
        )

    def test_create_signing_object_static_method(self):
        SigningsController.create_signing_object(
            signing=self.signing
        )

        self.assertIsNotNone(
            SigningsController.get_signing_by_id(
                self.signing.id
            )
        )

    def test_user_cant_signing_more_than_two_visitor(self):
        # First from setup
        SigningsController.create_signing_object(self.signing)
        # Second using static method
        SigningsController.create_signing(
            self.building, self.student,
            Student("Jason", "Terry", "M444444444"),
            self.employee
        )

        with self.assertRaises(HostRoomFull):
            # Third using static method
            SigningsController.create_signing(
                self.building, self.student,
                Student("Stephen", "Curry", "S666666"),
                self.employee
            )

    def test_if_visitor_is_not_in_system(self):
        visitor = Visitor(
            "Kevin", "Hart", "R444444",
            datetime.date.today(),
            "190 Main St Lawrence, MA 01233"
        )
        signing = Signing(self.building, self.student,
                          visitor, self.employee)
        signing_controller = SigningsController(signing)
        self.assertIsNone(
            VisitorController.get_visitor_by_visitor_id(
                visitor.id
            )
        )

        with self.assertRaises(VisitorNoInSystem):
            # Try the static method
            SigningsController.create_signing(
                self.building,
                self.student,
                visitor,
                self.employee
            )
        with self.assertRaises(VisitorNoInSystem):
            # Try the static method that use the object
            SigningsController.create_signing_object(signing)
        with self.assertRaises(VisitorNoInSystem):
            # Try the member method of the controller
            signing_controller.create()

    def test_if_student_and_visitor_live_in_same_building(self):
        visitor = Student(
            "Manny", "Ramirez", "A009090", self.student.building
        )
        signing = Signing(
            self.building,
            self.student,
            visitor,
            self.employee
        )
        signing_controller = SigningsController(signing)

        with self.assertRaises(VisitorLiveHere):
            SigningsController.create_signing(
                self.building, self.student, visitor, self.employee
            )
        with self.assertRaises(VisitorLiveHere):
            SigningsController.create_signing_object(signing)
        with self.assertRaises(VisitorLiveHere):
            signing_controller.create()
