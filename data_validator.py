import re
from employee import Employee
from time import strptime
# This module provides various time-related functions.


class DataValidator:

    def __init__(self):
        self.validators = (
            self.check_empid,
            self.check_gender,
            self.check_age,
            self.check_sales,
            self.check_bmi,
            self.check_salary,
            self.check_birthday
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

        # Check if there are combination of [A-Z][0-9]{3} e.r E111
        # :P<empid> Assign to the group with the keyword 'empid'
        pattern = r"\D*(?P<empid>[A-Z][0-9]{3})\D*"
        match_obj = re.search(pattern, empid, re.I)
        if match_obj:
            empid = match_obj.group("empid")
            # Get the matching word
            return empid.upper()
            # Convert the first letter to Uppercase and the rest is lowercase
        return None
        # return None if match not found

    @staticmethod
    def check_gender(input_gender):
        """
        Check valid employee gender
        :param input_gender:
        :return:
        Written By: Vaishali Patel
        """
        pattern_01 = r"^(?P<gender>F\w*|M\w*)$"
        pattern_02 = r"^(?P<gender>girl\boy)$"
        match_01 = re.match(pattern_01, input_gender, re.I)
        result = None
        if match_01:
            gender = match_01.group("input_gender").upper()
            result = gender[0]
        else:
            match_02 = re.match(pattern_02, input_gender, re.I)
            if match_02:
                gender = match_02.group("input_gender").upper()
                result = "F" if input_gender == "GIRL" else "M"
        return result

    @staticmethod
    def check_age(input_age):
        """
        check valid employee age
        :param input_age:
        :return:
        Written By: Vaishali Patel
        """
        pattern = r"^(?P<age>[0-9]{2})$"
        match_obj = re.match(pattern, input_age)
        if match_obj:
            return int(match_obj.group("input_age"))
            # Convert the match obj to integer and
            # Return Non if matches not found
        return None

    @staticmethod
    def check_sales(input_sales):
        """
        check valid employee sales
        :param input_sales:
        :return:
        Written By: Vaishali Patel
        """
        # Regular expression checks if there are consecutive 3 numbers
        # :P<sales> Assign to the group with the keyword 'sales'
        pattern = r"\D*(?P<sales>[0-9]{2,3})\D*"
        match_obj = re.search(pattern, input_sales)
        if match_obj:
            # Convert the match to integer
            return int(match_obj.group("input_sales"))
        # Return None if no match found
        return None

    @staticmethod
    def check_bmi(input_bmi):
        """
        Check valid employee bmi
        :param input_bmi:
        :return:
        """
        # First convert the user input bmi into string
        bmi = str(input_bmi)

        # Regular expression check if any of the specified keywords exists
        # :P<bmi> Assign to the group with the keyword 'bmi'
        pattern = r".*(?P<bmi>normal|overweight|obesity|underweight).*"
        match_obj = re.search(pattern, bmi, re.I)
        if match_obj:
            bmi = match_obj.group("input_bmi")
            # Convert the first letter to uppercase and the rest is lowercase
            bmi = " ".join(text[0].upper() + text[1:] for text in bmi.split())
            return bmi
        # Return None if no match found
        return None

    @staticmethod
    def check_salary(input_salary):
        """
        Check valid salary
        :param input_salary:
        :return:
        Written By: Vaishali Patel
        """
        # Regular expression checks if there are consecutive 3 numbers
        # :P<salary> Assign to the group with the keyword 'salary'
        pattern = r"\D*(?P<salary>[0-9]{2,3})\D*"
        match_obj = re.search(pattern, input_salary)
        if match_obj:
            # Convert the match to integer and return
            return int(match_obj.group("salary"))
        # Return None if no match found
        return None

    @staticmethod
    def check_birthday(input_birthday):
        """
        Check validation of birthday
        :param birthday: <String>
        :return: washed data
        Written By: Vaishali Patel
        """
        pattern = r"^([0-9]{1,2})[-/\.]([0-9]{1,2})[-/\.]([0-9]{2}|[0-9]{4})$"
        match = re.match(pattern, input_birthday)
        if match:
            date = "-".join(match.groups())
            format = strptime(date, "%d-%m-%Y")
            return "{0}-{1}-{2}".format(
                            format.tm_mday, format.tm_mon, format.tm_year
                            )
        else:
            return None

    def check_all(self, all_data: list):
        """
        Check validation of the all data.
        :param all_data: a data list
        :return: washed data in dictionary
        Written By: Vaishali Patel
        """
        result = []

        # If the number of the data is not correct, return an empty result
        if not len(all_data) == len(Employee):
            return result

        # Check and wash data
        key = 0
        while key < len(all_data):
            # Get the validation function by the order of the data
            v = self.validators[key]
            # Append to the result
            result.append(v(all_data[key]))
            key += 1

        return result

