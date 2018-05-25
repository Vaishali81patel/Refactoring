import unittest
from data import *

class EmployeeDataFormatTests(unittest.TestCase):
    """ test for data.py"""

    @classmethod
    def setUpClass(cls):
        print ("called once before any tests in class")

    @classmethod
    def tearDownClass(cls):
        print ("\ncalled once after all tests in class")

    def setUp(self):
        self.EMPID = 0
        self.GENDER = 1
        self.AGE = 2
        self.SALES = 3
        self.BMI = 4
        self.SALARY = 5
        self.BIRTHDAY = 6

    def tearDown(self):
        print ("\nend of test")

    def test_total_fields(self):
        values = [0, 1, 2, 3, 4, 5, 6]
        data_values = list(map(lambda i: i.value, Data))
        self.assertListEqual(data_values, values)

    def test_regular_empid_expression(self):
        self.assertRegex ("her empiidis$A333", r".*(?P<empid>[A-Z][0-9]{3}).*")

    def test_regular_gender_expression(self):
        self.assertRegex ("her genderis$F", r".*(?P<gender>F\w*|M\w*).*")

    def test_regular_age_expression(self):
        self.assertRegex ("her ageis$28", r".*(?P<age>[0-9]{2}).*")

    def test_regular_sales_expression(self):
        self.assertRegex ("her salesis$555", r".*(?P<sales>[0-9]{2,3}).*")

    def test_regular_bmi_expression(self):
        self.assertRegex ("heisoverweight$3333", r".*(?P<bmi>normal|overweight|obesity|underweight).*")

    def test_regular_salary_expression(self):
        self.assertRegex ("her salesis$999", r".*(?P<salary>[0-9]{2,3}).*")

   # def test_regular_birthday_expression(self):
    #    self.assertRegex ("her birthdayis$12-12-2000", r"\D*(?P<birthday>[0-9]{1,2})[-/\.]([0-9]{1,2})[-/\.]([0-9]{2}|[0-9]{4}\D*")


if __name__ == '__main__':
    unittest.main ()
