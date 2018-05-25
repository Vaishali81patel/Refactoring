from data import Data
from employee_data import EmployeeData

class GetEmployee(EmployeeData):

    def __init__(self):
      #  print ('Delegation works!!.')
        super ().__init__()

    def get_all_data(self):
        return self.data + self.new_data

    def displayCount(self):
        GetEmployee.empCount

    def get_gender(self):
        """
        Get gender statistics
        :return: <Dictionary> gender
        :Author: Vaishali Patel
        """
        all_data = self.get_all_data()
        if len(all_data) == 0:
            return {}

        male = 0
        female = 0
        for row in all_data:
            # Calculate sum of male
            if row[Data.GENDER.name] == "M":
                male += 1
            # Calculate sum of female
            else:
                female += 1

        return {"Male": male, "Female": female}

    def get_bmi(self):
        bmi = {}

        all_data = self.get_all_data()
        if len(all_data) == 0:
            return bmi

        for row in all_data:
            if row[Data.BMI.name] not in bmi.keys():
                bmi[row[Data.BMI.name]] = 1
            else:
                bmi[row[Data.BMI.name]] += 1
        return bmi

    def get_salary(self):
        salary = {}

        all_data = self.get_all_data()
        if len(all_data) == 0:
            return salary

        for row in all_data:
            if row[Data.SALARY.name] not in salary.keys():
                salary[row[Data.SALARY.name]] = 1
            else:
                salary[row[Data.SALARY.name]] += 1
        return salary

    def __del__(self):
        self.data = []
        self._source = None
