from cmd import Cmd
from IDatabase import *
# from csv import Error as CSVError
# from view_console import ViewConsole as View
# from emplyee_data import EmpolyeeData
# from employee import Employee
# import string
#import sys
# import os
# Import os Executing a shell command os.system \
# function Get the users environment os.


class CLI(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '>>> '
        self.intro = "WELCOME TO THE EMPLOYEE HELP CONSOLE!"

        # object of DataValidator for validating employee data
        self._valid = DataValidator()

        # Instance of EmployeeData
        # self._std = EmployeeData()

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a \
           list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        # The only reason to define this method is \
        # for the help text in the doc string
        cmd.Cmd.do_help(self, args)

    def do_quit(self, arg):
        """ Exits from the Console!"""
        sys.exit(1)

    def help_quit(self):
        """ Get the help on Quit"""
        print('THANKS FOR USING CONSOLE! BYE')
        sys.exit(1)

    # shortcuts
    do_q = do_quit

    # Command definitions to \
    # support Cmd object functionality \
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(self, args)

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    def do_add(self, s):
        print('This command adds the employee data to the system.')
        print('USAGE:')
        print('add< EMPID >< GENDER >< AGE >')
        print ('< SALES >< BMI >< SALARY >< BIRTHDAY >')
        print("""***DATA FORMAT:
                    EMPID..........[A-Z][0-9]{3} e.x.: M123
                    GENDER.........(M|F)  e.x.: F      \
                    AGE............[0-9]{2}  e.x.: 28  \
                    SALES..........[0-9]{3} e.x.: 100  \
                    BMI............(Normal|Overweight|Obesity|Underweight) \
                                e.x.: Normal
                    SALARY.........[0-9]{2-3} e.x.: 200
                    BIRTHDAY.......[1-31]-[1-12]-[0-9]{4} \
                                e.x.: 1990-10-21' """)

    def do_save(self, s):
        print('save command saves the current employee data to the system.')
        print('USAGE:')
        print('save < FILENAME >')

    def do_show(self, s):
        print('show command displays the current')
        print('working employee information in a specified format.')
        print('USAGE:')
        print('show < -OPTION > < OBJECT >')

    def help_add(self):
        print("""*** OPTIONS
            -l : This option loads the employee information from a file. \
                 The file is given to the command as a string.
            -m : This option does manual data entry. The user will be \
                 prompted for step by step employee information \
                 to be entered into the system.
            -d : This option loads the employee information \
                 into the system from a database.
            ***""")

    def help_save(self):
        print("""*** OPTIONS
                -s : This option is a standard save. The information is \
                     saved to a file in the existing program files.
                -d : This option saves the current employee \
                     information to the database.
                -f : This option saves a file to the specific file location.
            ***""")

    def help_show(self):
        print("""*** OPTIONS
            -a : This option shows a bar graph of the total sales made \
                 by males verse the total sales made by female.
            -b : This option shows a pie chart of the percentage \
                 of female workers verse male workers
            -c : This option shows a scatter plot graph of \
                 peoples age verse their salary.
            -d : This option shows a pie chart of the BMI of a set of people.
            ***""")
cli = CLI()
cli.cmdloop()

