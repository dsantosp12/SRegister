from app.person.model import *
from app.building.model import *
from app.signings.model import *

host = Student("Danie", "Santos", "1234")
visitor = Visitor("Test", "Test", "1234123", "11-22-1993", "123 Mian")
employee = Employee("Juslio", "hernandex", "jhernan", "123456", "21341234",
                    "test@test.com")
building = Building("ICC")

sign = Signing(building, host, visitor, employee)

print(sign)