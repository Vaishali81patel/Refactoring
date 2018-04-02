import re
from employee import Employee
from time import strptime
# This module provides various time-related functions.


class DataValidator:

    def __init__(self):
        self.validators =(
            self.check_empid,
            self.check_gendeer,
            self.check_age,
            self.check_sales,
            self.check_bmi,
            self.check_salary,
            self.birthday
        )

    @staticmethod
    def check_empid(input_empid):
        """
        Validate user input empid
        :param input_empid:
        :return:
        Written By: Vaishali Patel
        """
        # Convert the input employee id to string
        empid = str(input_empid)

        # check if there are combination of [A-Z][0-9]{3} e.r E111
        
