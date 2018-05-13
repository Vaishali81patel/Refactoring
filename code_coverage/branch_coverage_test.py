import unittest
from employee_data import EmplopyeeData
import sys
from io import StringIO
from contexlib import contextmanager

class EmployeeDataUnitTests(unittest.TestCase):
    """
    http://istqbexamcertification.com/what-is-decision-coverage-its-advantages-and-disadvantages/#more-417
    """
    def setUp(self):
        self.employee_data = EmplopyeeData()
		print("A test case is called.")
		
	def tearDown(self):
		print ("This test case is done!")

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

			# ****************************************************************
			# ************************************************************************
			# employee_data	
	
	def test_employee_info_no_header(self):
        employees_list_no_header = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info(employees_list_no_header)
        # remove the header
        self.assertEqual(employees_list_no_header, result[0])

    def test_employee_info_with_header(self):
        employees_list_with_header = [
            ['empid', 'gender', 'age', 'sales', 'bmi', 'salary', 'dob'],
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info(employees_list_with_header)
        # remove the header
        employees_list_with_header.pop(0)
        self.assertEqual(employees_list_with_header, result[0])
        self.assertEqual([], result[1])

    

if __name__ == '__main__':
    unittest.main(verbosity=2)
