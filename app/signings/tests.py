import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as SeleniumException


class TestSignInViews(unittest.TestCase):
    def test_sign_in_existing_visitor(self):
        self.fill_in_visitor()
        self.submit_form()
        self.assertIn("Sign In Created Successfully", self.driver.page_source)

    def test_sign_in_room_full(self):
        # First Visitor
        self.fill_in_visitor()
        self.submit_form()
        # Second Visitor
        self.fill_in_visitor()
        self.submit_form()
        # Third Visitor
        self.fill_in_visitor()
        self.submit_form()
        self.assertIn("Host already has two visitor", self.driver.page_source)

    def submit_form(self):
        self.driver.find_element_by_id("submit_signin").send_keys(Keys.ENTER)
        self.driver.find_element_by_id("submit_signin_last").send_keys(Keys.ENTER)

    def clear_form(self):
        self.driver.find_element_by_id("clear_form").click()

    def fill_in_visitor(self):
        self.driver.get("http://0.0.0.0:5000/dashboard/sign-in-visitor")
        # Select the fields in the form
        self.driver.find_element_by_id("visitor_id").send_keys("001")
        self.driver.find_element_by_id("first_name").send_keys("John")
        self.driver.find_element_by_id("last_name").send_keys("Smith")
        self.driver.find_element_by_id("date_of_birth").click()
        # Select month and year
        month = Select(self.driver.find_element_by_class_name("picker__select--month"))
        month.select_by_visible_text("June")
        year = Select(self.driver.find_element_by_class_name("picker__select--year"))
        year.select_by_value("1983")
        # Select a day
        self.driver.find_element_by_xpath("//table[@id='date_of_birth_table']").click()
        self.driver.find_element_by_id("street_name").send_keys("123 Main St")
        self.driver.find_element_by_id("city_state").send_keys("Icy, MA")
        self.driver.find_element_by_id("host_id").send_keys("01443782")
        self.driver.find_element_by_id("host_room").send_keys("231")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(800, 1000)
        self.driver.implicitly_wait(5)
        self.driver.get("http://0.0.0.0:5000/login/")
        try:
            self.driver.find_element_by_id("username").send_keys("developer")
            self.driver.find_element_by_id("password").send_keys("1234567890")
            self.driver.find_element_by_id("submit_login").send_keys(Keys.ENTER)
        except SeleniumException.NoSuchElementException:
            print("Looks like already signed in!")
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)
        self.driver.close()

"""
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
"""

if __name__ == '__main__':
    unittest.main()
