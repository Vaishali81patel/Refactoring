from data import Data
from file_handler import FileHandler
from database import Database

class GetEmployeeData:
    """
    For data related operations
    """
    def __init__(self):
        self.data = []
        self._source = None

def get_all_data(self):
        return self.data + self.new_data

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

    def __del__(self):
        self.data = []
        self._source = None
