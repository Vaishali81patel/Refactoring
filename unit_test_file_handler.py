from unittest import TestCase, main
from file_handler import FileHandler
from data import Data
from data_validator import DataValidator
from data import Data


class FileHandlerTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_csv_file_handler(self):
        csv = FileHandler("staffinfo.csv")
        self.assertTrue(type(csv._fieldnames) == list)

    def test_file_data_format(self):
        csv = FileHandler("staffinfo.csv")
        items = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        self.assertListEqual(csv._fieldnames, items)

    def test_file_lambda_type(self):
        items = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        data_keys = list(map(lambda i: i.name, Data))
        self.assertListEqual(data_keys, items)

    def test_file_lambda_type_value_store(self):
        values = [0, 1, 2, 3, 4, 5, 6]
        data_values = list(map(lambda i: i.value, Data))
        self.assertListEqual(data_values, values)

    def test_file_exists(self):
        csv = FileHandler("staffinfo2.csv")
        self.assertFalse(csv.file_exist())

    def test_read_data_from_file_has_attr(self):
        self.assertTrue(hasattr(FileHandler, "read"))

    def test_save_data_to_file_has_attr(self):
        self.assertTrue(hasattr(FileHandler, "save"))

    def test_read_data_to_file_get_attr(self):
        self.assertTrue(callable(getattr(FileHandler, "read")))

    def test_save_data_to_file_get_attr(self):
        self.assertTrue(callable(getattr(FileHandler, "save")))

    def test_file_type_error(self):
        csv = FileHandler("staffinfo.csv")
        self.assertRaises(AttributeError, csv.save, "This is a data list")

    def test_save_data_in_list_format(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertTrue(type(csv.read()) == list)

if __name__ == "__main__":
    main()

