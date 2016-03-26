import unittest
import datetime

from app.person.model import *
from app.person.person import *


class TestPersonModel(unittest.TestCase):
    """Unit test for the Person model"""

    def setUp(self):
        self.person = Person("John", "Smith")

    def test_first_name_field(self):
        self.assertEqual("John", self.person.first_name)

    def test_last_name_field(self):
        self.assertEqual("Smith", self.person.last_name)


class TestStudentModel(unittest.TestCase):
    """Unit test for the Student model"""

    def setUp(self):
        self.student = Student("Daniel", "Santos", "00132623")

    def test_student_id_field(self):
        self.assertEqual("00132623", self.student.student_id)


class TestStudentController(unittest.TestCase):

    def setUp(self):
        self.student_controller = StudentController("A00270354")

    def tearDown(self):
        StudentController.delete_student(
            self.student_controller.student_id
        )

    def test_create_student_method(self):
        self.student_controller.create()

        self.assertIsNotNone(
            StudentController.get_student_by_student_id(
                self.student_controller.student_id
            )
        )

    def test_create_student_static_method(self):
        StudentController.create_student("Tom", "Hill", "A002345")

        self.assertIsNotNone(
            StudentController.get_student_by_student_id(
                "A002345"
            )
        )

    def test_modify_student_first_name_static_method(self):
        StudentController.modify_first_name(
            student_id=self.student_controller.student_id,
            new_first_name="Tony"
        )

        self.assertEqual(
            StudentController.get_student_by_student_id(
                self.student_controller.student_id
            ).first_name,
            "Tony"
        )

    def test_modify_student_last_name_static_method(self):
        StudentController.modify_last_name(
            student_id=self.student_controller.student_id,
            new_last_name="Daron"
        )

        self.assertEqual(
            StudentController.get_student_by_student_id(
                self.student_controller.student_id
            ).last_name,
            "Daron"
        )

    def test_modify_student_id_static_method(self):
        StudentController.modify_student_id(
            old_id=self.student_controller.student_id,
            new_id="A999999999"
        )

        self.assertIsNotNone(
            self.student_controller.get_student_by_student_id(
                "A999999999"
            )
        )

        self.student_controller.student_id = "A999999999"

    def test_delete_student_static_method(self):
        StudentController.delete_student(
            self.student_controller.student_id
        )

        self.assertIsNone(
            StudentController.get_student_by_student_id(
                self.student_controller.student_id
            )
        )


class TestVisitorModel(unittest.TestCase):
    """Unit test for the Visitor model"""

    def setUp(self):
        self.visitor = Visitor(
            "John", "Smith",
            "S16632394", datetime.date.today(),
            "123 Main St Lowell, MA 01843"
        )

    def test_date_of_birth_field(self):
        self.assertEqual(datetime.date.today(), self.visitor.date_of_birth)

    def test_address_field(self):
        self.assertEqual("123 Main St Lowell, MA 01843", self.visitor.address)


class TestVisitorController(unittest.TestCase):

    def setUp(self):
        self.visitor = Visitor(
            "John", "Smith",
            "S16632394", datetime.date.today(),
            "123 Main St Lowell, MA 01843"
        )
        self.visitor_controller = VisitorController(
            self.visitor
        )

    def tearDown(self):
        VisitorController.delete_visitor(self.visitor)

    def test_create_visitor_method(self):
        self.visitor_controller.create()

        self.assertIsNotNone(
            VisitorController.get_visitor_by_visitor_id(
                visitor_id=self.visitor.visitor_id
            )
        )

    def test_create_visitor_object_static_method(self):
        VisitorController.create_visitor_object(self.visitor)

        self.assertIsNotNone(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            )
        )

    def test_create_visitor_static_method(self):
        VisitorController.create_visitor(
            first_name=self.visitor.first_name,
            last_name=self.visitor.last_name,
            visitor_id=self.visitor.visitor_id,
            date_of_birth=self.visitor.date_of_birth,
            address=self.visitor.address
        )

        self.assertIsNotNone(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            )
        )

    def test_modify_visitor_first_name_method(self):
        first_name = "Daron"
        VisitorController.modify_first_name(
            visitor_id=self.visitor.visitor_id,
            new_first_name=first_name
        )

        self.assertEqual(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            ).first_name,
            first_name
        )

    def test_modify_visitor_last_name_static_method(self):
        last_name = "Duke"
        VisitorController.modify_last_name(
            visitor_id=self.visitor.visitor_id,
            new_last_name=last_name
        )

        self.assertEqual(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            ).last_name,
            last_name
        )

    def test_modify_visitor_visitor_id_static_method(self):
        new_visitor_id = "Z9999999"
        VisitorController.modify_visitor_id(
            old_visitor_id=self.visitor.visitor_id,
            new_visitor_id=new_visitor_id
        )

        self.assertIsNotNone(
            VisitorController.get_visitor_by_visitor_id(
                new_visitor_id
            )
        )

        self.visitor.visitor_id = new_visitor_id

    def test_modify_visitor_address_static_method(self):
        address="18 Hill St Havering, MA 10844"
        VisitorController.modify_visitor_address(
            visitor_id=self.visitor.visitor_id,
            new_address=address
        )

        self.assertEqual(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            ).address,
            address
        )

    def test_modify_visitor_date_of_birth(self):
        new_date = datetime.date(2016, 23, 9)
        VisitorController.modify_visitor_date_of_birth(
            visitor_id=VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            ),
            new_date_of_birth=new_date
        )

        self.assertEqual(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            ).date_of_birth,
            new_date
        )

    def test_delete_visitor_static_method(self):
        VisitorController.delete_visitor(
            visitor_id=self.visitor.visitor_id
        )

        self.assertIsNone(
            VisitorController.get_visitor_by_visitor_id(
                self.visitor.visitor_id
            )
        )

if __name__ == '__main__':
    unittest.main()
