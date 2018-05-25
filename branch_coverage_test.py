import unittest
from employee_data import EmployeeData
import sys
import os
from io import StringIO
# from contexlib import contextmanager

# sys.path.append(os.path.abspath('../Refactoring'))



class EmployeeDataUnitTests(unittest.TestCase):
    """
    http://istqbexamcertification.com/what-is-decision-coverage-its-advantages-and-disadvantages/#more-417
    """
    def setUp(self):
        self.employee = EmployeeData()
		# print("A test case is called")
		
        # ****************************************************************
        # ************************************************************************
        # employee_data

    def tearDown(self):
        print ("This test case is done!")


    def test_employee_info_no_header(self):
        employees_data_no_header = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info (employees_data_no_header)
        # remove the header
        self.assertEqual (employees_list_no_header, result[0])

    def test_employee_info_with_header(self):
        employees_data_with_header = [
            ['empid', 'gender', 'age', 'sales', 'bmi', 'salary', 'dob'],
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.data (employees_data_with_header)
        # remove the header
        employees_list_with_header.pop (0)
        self.assertEqual (employees_data_with_header, result[0])
        self.assertEqual ([], result[1])

    def test_employee_info_same_empid(self):
        employees_data_duplicate_id = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['A123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info (employees_data_duplicate_id)
        # remove duplicate record
        employees_data_duplicate_id.pop (1)
        self.assertEqual (employees_data_duplicate_id, result[0])
        self.assertEqual ([['Record 2', 'EmpID not unique']], result[1])

    def test_employee_info_invalid_record(self):
        employees_data_invalid_record = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'X', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info (employees_data_invalid_record)
        # remove invalid record
        employees_data_invalid_record.pop (1)
        self.assertEqual (employees_data_invalid_record, result[0])
        # error list
        self.assertEqual ([['Record 2', 'Gender : Not M or F']], result[1])




if __name__ == '__main__':
    unittest.main ()
