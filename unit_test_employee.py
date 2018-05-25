from unittest import TestCase, main
from file_handler import FileHandler
from data import Data
from data_validator import DataValidator
from employee_data import EmployeeData


class EmployeeUnitTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_file_extention(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertTrue(type(csv._fieldnames) == list)

    def test_valid_fields(self):
        csv = FileHandler("employeeinfo.csv")
        items = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        self.assertListEqual(csv._fieldnames, items)

    def test_lambda_map_data_keys(self):
        items = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        data_keys = list(map(lambda i: i.name, Data))
        self.assertListEqual(data_keys, items)

    def test_total_fields(self):
        values = [0, 1, 2, 3, 4, 5, 6]
        data_values = list(map(lambda i: i.value, Data))
        self.assertListEqual(data_values, values)

    def test_file_available(self):
        csv = FileHandler("employeeinfo2.csv")
        self.assertTrue(csv.file_exist())

    def test_file_read(self):
        self.assertTrue(hasattr(FileHandler, "read"))

    def test_file_save(self):
        self.assertTrue(hasattr(FileHandler, "save"))

    def test_can_read_file(self):
        self.assertTrue(callable(getattr(FileHandler, "read")))

    def test_can_save_file(self):
        self.assertTrue(callable(getattr(FileHandler, "save")))

    def test_all_data_valid(self):
        vld = DataValidator()
        self.assertTrue(len(vld.validators) == 7)

    def test_employee_data_list(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertRaises(AttributeError, csv.save, "This is a data list")

    def test_regular_expression(self):
        self.assertRegex("heisoverweight$3333", r".*(?P<bmi>normal|overweight|obesity|underweight).*")

    def test_regular_date_expression(self):
        self.assertRegex("her salaryis$333last year", r"\D*(?P<salary>[0-9]{2,3})\D*")

    def test_read_csv_file_list(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertTrue(type(csv.read()) == list)

    def test_source_data(self):
        employee_data = EmployeeData()
        employee_data.select_source("csv", "employeeinfo.csv")
        self.assertIsInstance(employee_data._source, FileHandler)

    def test_valid_source(self):
        employee_data = EmployeeData()
        employee_data.select_source("source")
        self.assertIsNone(employee_data._source)

    def test_raise_error(self):
        employee_data = EmployeeData()
        self.assertRaises(OSError, employee_data.save_data)

    def test_data_exists(self):
        employee_data = EmployeeData()
        employee_data.data = [{
            "EMPID": "T123",
            "AGE": 33,
            "GENDER": "M",
            "SALES": 200,
            "BMI": "Normal",
            "SALARY": 200,
            "BIRTHDAY": "31-12-1985"}]
        new_data = ["T123", 26, "F", 150, "Normal", 100, "01-01-1992"]
        self.assertTrue(employee_data.data_exist(new_data))


if __name__ == "__main__":
    main()
