import unittest
from interpreter_controller import InterpreterController
from employee_data import EmployeeData
# from io import StringIO
import os


class ControllerUnitTests(unittest.TestCase):
    def setUp(self):
        self.ctrl = InterpreterController(EmployeeData())

    def tearDown(self):
        print("This test case is done!")

# check_file_name_extensions
    def test_check_file_name_extensions_db(self):
        self.assertTrue(self.ctrl.check_file_name_extensions
                        ('data/data_employee.db', 'input'))
"""
    def test_check_file_name_extensions_csv(self):
        self.assertTrue(self.ctrl.check_file_name_extensions
                        ('data/employee.csv', 'input'))

    def test_check_file_name_extensions_txt_input(self):
        self.assertFalse(self.ctrl.check_file_name_extensions
                         ('data/employee.txt', 'input'))

    def test_check_file_name_extensions_txt_output(self):
        self.assertFalse(self.ctrl.check_file_name_extensions
                         ('data/employee.txt', 'output'))

    def test_check_file_name_extensions_db_output(self):
        self.assertTrue(self.ctrl.check_file_name_extensions
                         ('data/employee.db', 'output'))

    # *********************************************************************
    # check_file_exists
    def test_check_file_exists_valid_file(self):
            self.assertTrue(self.ctrl.check_file_exists
                             ('data/data_02.csv'))

    def test_check_file_exists_invalid_file(self):
        self.assertFalse(self.ctrl.check_file_exists
                        ('data/xx.csv'))
"""

if __name__ == '__main__':
    unittest.main()
