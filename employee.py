# Create an employee class
from enum import Enum, unique
# The enum module defines an enumeration
# type with iteration and comparison
# capabilities. It can be used to create
# well-defined symbols for values,
# instead of using literal integers or strings.


@unique
class Employee(Enum):
    """
    Enum for employee data store
    """
    EMPID = 0
    GENDER = 1
    AGE = 2
    SALES = 3
    BMI = 4
    SALARY = 5
    BIRTHDAY = 6
