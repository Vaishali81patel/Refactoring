# coding=utf-8
from employee import Employee
from file_handler import FileHandler
from database import Database

class EmployeeData:
    """
    This class enable to do employee data related operation and access
    """
    def __init__(self):
        self.emp_data = []
        self.new_emp_data = []
        self.data_source = None

    def select_source(self, data_source, file_path=None, create=False):
        """
        This function enable to initialize employee data and file source
        :param data_source: <string>
        :param file_path: <string>
        :param create: <Boolean>
        :return: None
        : Written By: Vaishali Patel
        """
        # Set data source
        if data_source == "csv":
            self.data_source = FileHandler(file_path, create)
            self.load_data()
        if data_source == "db":
            self.data_source = Database()
            self.load_data()


    def load_data(self):
        """
        Retrieved / Fetch all the data from the specified data source
        :return: None
        Written By: Vaishali Patel
        """
        # When fetch data from the data source
        # move existed data in self.emp_data to the end of the list
        self.new_emp_data = self.data_source.read()
        # else:
        # old_emp_data = self.emp_data
        # self.emp_data = self._data_source.read()
        # self.emp_data += old_emp_data


    def add_data(self, emp_data):
        """
        This function enable to add data to self.emp_data
        """
        if not self.data_exist(emp_data):
            # Append to the temporary emp data
            # self.emp_data.append ({d.name:data[d.value] for e in Employee}
            self.new_emp_data.append({d.name: emp_data[d.value] for d in Employee})
        else:
            # If the EMPID is exists, raise an exception
            raise AttributeError("The EMPID is already exists.")

    def data_exist(self, emp_data):
        """
        This function enable to check if the data with same empid is exist
        :param emp_data:
        :return:
        """
        for employee in self.emp_data:
            if emp_data[int(Employee.EMPID.value)] == employee[Employee.EMPID.name]:
                return True

        for employee in self.new_emp_data:
            if emp_data[int(Employee.EMPID.value)] == emp_data[Employee.EMPID.name]:
                return True
        return

    def save_data(self):
        """
        This function enable to save data
        :return:
        """
        if self.data_source is None:
            raise OSError("No data source is specified.")

        if len(self.new_emp_data) == 0:
            raise ValueError("No data to save.")

        try:
            self.data_source.save(self.new_emp_data)
        except Exception as e:
            raise IOError(e)
        else:
            # Reset temp data and reload data from the data source
            self.new_emp_data = []
            self.load_data()

    def get_all_emp_data(self):
        return self.emp_data + self.new_emp_data

    def get_gender(self):
        """
        This function enable to get gender statistics
        :return:
        """
        all_emp_data =  self.get_all_emp_data()
        if len(all_emp_data) == 0:
            return {}

        male = 0
        female = 0
        for row in all_emp_data:
            # Calculate male employee
            if row[Employee.GENDER.name] == "M":
                male += 1
            # Calculate female employee
            else:
                female += 1
        return {"Male" :male, "Female": female}


    def get_bmi(self):
        bmi = {}

        all_emp_data = self.get_all_emp_data()
        if len(all_emp_data) == 0:
            return bmi

        for row in all_emp_data:
            if row[Employee.BMI.name] not in bmi.keys():
                bmi[row[Employee.BMI.name]] = 1
            else:
                bmi[row[Employee.BMI.name]] += 1
        return bmi

    def __del__(self):
        self.emp_data = []
        self.data_source = None



