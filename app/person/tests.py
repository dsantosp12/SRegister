import unittest
import datetime

from app.person.model import *


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


if __name__ == '__main__':
    unittest.main()
