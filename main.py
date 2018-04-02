from interpreter_controller import *
from view import *
from interpreter import *
from file_handler import *
from emp_data_validator import *
from database import *
import sys

if __name__ == '__main__':
    InterpreterController(EmployeeData_View(), Interpreter(
        FileHandler(), DataValidator(), Database(),
        InterpreterController.set_file_path(sys.argv))).cmdloop()

# sys.argv is a list in Python,
# which contains the command-line
# arguments passed to the script.
# With the len(sys.argv) function
# you can count the number of arguments.
