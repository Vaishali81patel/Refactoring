import unittest
from data_validator import *


class DataValidatorTests (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dataValidator = DataValidator()

    def setUp(self):
        # be executed before each test
        print ("set up")
        self.data = [['A001', 'F', '25', '550', 'Normal', '39', '30-05-1995'],
                     ['C333', 'M', '5', '777', 'Overweight', '300', '1-12-1977'],
                     ['D4', 'Male', 'nine', '66,9', 'heavy', '5,00', '1-12-19']]

        self.data_2 = [['H001', 'M', '18', '200', 'Normal', '250', '29-05-1999']]

        self.data_3 = [['', '', '', '', '', '', '']]

        self.data_4 = [['I001', 'Male', 'eight', '1oo', 'Normal', '245', '30-06-1999']]

        self.data_5 = [['@001', '~', '!', '&&&', '^', '$', '*-10-*']]

    def tearDown(self):
        # be executed after each test case
        print ("teardown")

    # Test 01
    def test_data_validator_01(self):
        # good day for testing validator
        result = [['H001', 'M', '16', '200', 'Normal', '230', '30-05-1999']]
        self.assertEqual (self.dataValidator.validate_data (self.data_2), result, "That is not a valid data array")

    # Test 02
    def test_data_validator_02(self):
        # bad day for testing validator no data
        result = []
        self.assertEqual (self.dataValidator.validate_data (self.data_3), result, "That is not a valid data array")

    # Test 03
    def test_data_validator_03(self):
        # bad day for testing validator some data
        result = []
        self.assertEqual (self.dataValidator.validate_data (self.data_4), result, "That is not a valid data array")

    # Test 04
    def test_data_validator_04(self):
        # bad day for testing validator can it handle special characters
        result = []
        self.assertEqual (self.dataValidator.validate_data (self.data_5), result, "That is not a valid data array")

    # Test 05
    def test_employee_age_01(self):
        # good day test for employee 1
        age = self.data[0][2]
        self.assertTrue (self.dataValidator.validate_age (age), "That is not a valid age input")

    # Test 06
    def test_employee_age_02(self):
        # good day test for employee 2
        age = self.data[1][2]
        self.assertFalse (self.dataValidator.validate_age (age), "That is not a valid age input")

    # Test 07
    def test_employee_age_03(self):
        # bad day test for employee 3 bad data is rejected
        age = self.data[2][2]
        self.assertFalse (self.dataValidator.validate_age (age), "That is not a valid age input")

    # Test 08
    def test_employee_empid_01(self):
        empid = self.data[0][0]
        self.assertTrue (self.dataValidator.validate_empid (empid), "This is a valid EmployeeID input")

    # Test 09
    def test_employee_empid_02(self):
        empid = self.data[1][0]
        self.assertTrue (self.dataValidator.validate_empid (empid), "This is a valid EmployeeID input")

    # Test 10
    def test_employee_empid_03(self):
        empid = self.data[2][0]
        self.assertFalse (self.dataValidator.validate_empid (empid), "This is  NOT a valid EmployeeID input")

    # Test 11
    # Testing valid gender input
    def test_employee_gender_01(self):
        gender = self.data[0][1]
        self.assertTrue (self.dataValidator.validate_gender (gender), "This is a valid Gender input")

    # Test 12
    def test_employee_gender_02(self):
        gender = self.data[1][1]
        self.assertTrue (self.dataValidator.validate_gender (gender), "This is a valid Gender input")

    # Test 13
    def test_employee_gender_03(self):
        gender = self.data[2][2]
        self.assertFalse (self.dataValidator.validate_gender (gender), "This is NOT a valid Gender input")

    # Test 14
    # Testing valid sales
    def test_employee_sales_01(self):
        sales = self.data[0][3]
        self.assertTrue (self.dataValidator.validate_sales (sales), "This is a valid Sales input")

    # Test 15
    def test_employee_sales_02(self):
        sales = self.data[1][3]
        self.assertTrue (self.dataValidator.validate_sales (sales), "This is a valid Sales input")

    # Test 16
    def test_employee_sales_03(self):
        sales = self.data[2][3]
        self.assertFalse (self.dataValidator.validate_sales (sales), "This is NOT a valid Sales input")

    # Test 17
    # Testing valid BMI input
    def test_employee_bmi_01(self):
        bmi = self.data[0][4]
        self.assertTrue (self.dataValidator.validate_bmi (bmi), "This is a valid BMI input")

    # Test 18
    def test_employee_bmi_02(self):
        bmi = self.data[1][4]
        self.assertTrue (self.dataValidator.validate_bmi (bmi), "This is a valid BMI input")

    # Test 19
    def test_employee_bmi_03(self):
        bmi = self.data[2][4]
        self.assertFalse (self.dataValidator.validate_bmi (bmi), "This is NOT a valid BMI input")

    # Test 20
    # Testing valid Salary input
    def test_employee_salary_01(self):
        salary = self.data[0][5]
        self.assertTrue (self.dataValidator.validate_salary (salary), "This is a valid Salary input")

    # Test 21
    def test_employee_salary_02(self):
        salary = self.data[1][5]
        self.assertTrue (self.dataValidator.validate_salary (salary), "This is a valid Salary input")

    # Test 22
    def test_employee_salary_03(self):
        salary = self.data[2][5]
        self.assertFalse (self.dataValidator.validate_salary (salary), "This is NOT a valid Salary input")

    # Test 23
    # Testing valid Birthday input
    def test_employee_birthday_01(self):
        birthday = self.data[0][6]
        self.assertTrue (self.dataValidator.validate_birthday (birthday), "This is a valid Birthday input")

    # Test 24
    def test_employee_birthday_02(self):
        birthday = self.data[1][6]
        self.assertTrue (self.dataValidator.validate_birthday (birthday), "This is a valid Birthday input")

    # Test 25
    def test_employee_birthday_03(self):
        birthday = self.data[2][6]
        self.assertFalse (self.dataValidator.validate_birthday (birthday), "This is NOT a valid Birthday input")

    # Test 26
    def test_employee_empid_01(self):
        empid = self.data[0][0]
        self.assertTrue (self.dataValidator.validate_empid (empid), "This is a valid EmployeeID input")

    # Test 27
    def test_employee_empid_02(self):
        empid = self.data[1][0]
        self.assertTrue (self.dataValidator.validate_empid (empid), "This is a valid EmployeeID input")

    # Test 28
    def test_employee_empid_03(self):
        empid = self.data[2][0]
        self.assertFalse (self.dataValidator.validate_empid (empid), "This is  NOT a valid EmployeeID input")

    # Test 29
    # Testing valid gender input
    def test_employee_gender_01(self):
        gender = self.data[0][1]
        self.assertTrue (self.dataValidator.validate_gender (gender), "This is a valid Gender input")

    # Test 30
    def test_employee_gender_02(self):
        gender = self.data[1][1]
        self.assertTrue (self.dataValidator.validate_gender (gender), "This is a valid Gender input")

    # Test 31
    def test_employee_gender_03(self):
        gender = self.data[2][2]
        self.assertFalse (self.dataValidator.validate_gender (gender), "This is NOT a valid Gender input")

    # Test 32
    # Testing valid sales
    def test_employee_sales_01(self):
        sales = self.data[0][3]
        self.assertTrue (self.dataValidator.validate_sales (sales), "This is a valid Sales input")

    # Test 33
    def test_employee_sales_02(self):
        sales = self.data[1][3]
        self.assertTrue (self.dataValidator.validate_sales (sales), "This is a valid Sales input")

    # Test 34
    def test_employee_sales_03(self):
        sales = self.data[2][3]
        self.assertFalse (self.dataValidator.validate_sales (sales), "This is NOT a valid Sales input")

    # Test 35
    # Testing valid BMI input
    def test_employee_bmi_01(self):
        bmi = self.data[0][4]
        self.assertTrue (self.dataValidator.validate_bmi (bmi), "This is a valid BMI input")

    # Test 36
    def test_employee_bmi_02(self):
        bmi = self.data[1][4]
        self.assertTrue (self.dataValidator.validate_bmi (bmi), "This is a valid BMI input")

    # Test 37
    def test_employee_bmi_03(self):
        bmi = self.data[2][4]
        self.assertFalse (self.dataValidator.validate_bmi (bmi), "This is NOT a valid BMI input")

    # Test 38
    # Testing valid Salary input
    def test_employee_salary_01(self):
        salary = self.data[0][5]
        self.assertTrue (self.dataValidator.validate_salary (salary), "This is a valid Salary input")

    # Test 39
    def test_employee_salary_02(self):
        salary = self.data[1][5]
        self.assertTrue (self.dataValidator.validate_salary (salary), "This is a valid Salary input")

    # Test 40
    def test_employee_salary_03(self):
        salary = self.data[2][5]
        self.assertFalse (self.dataValidator.validate_salary (salary), "This is NOT a valid Salary input")

    # Test 41
    # Testing valid Birthdate input
    def test_employee_birthday_01(self):
        birthday = self.data[0][6]
        self.assertTrue (self.dataValidator.validate_birthday (birthday), "This is a valid Birthday input")

    # Test 42
    def test_employee_birthday_02(self):
        birthday = self.data[1][6]
        self.assertTrue (self.dataValidator.validate_birthday (birthday), "This is a valid Birthday input")

    # Test 43
    def test_employee_birthday_03(self):
        birthday = self.data[2][6]
        self.assertFalse (self.dataValidator.validate_birthday (birthday), "This is NOT a valid Birthday input")


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main ()
