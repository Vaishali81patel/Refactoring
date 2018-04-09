from cmd import Cmd
from csv import Error as CSVError
from data_validator import DataValidator
from employee import Employee
from view_console import ViewConsole as View
from employee_data_access import EmployeeData
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
        self._std = EmployeeData()


    def do_select(self, line):
        """
        Select data from source
        :param self:
        :param line:
        :return:
        """
        # Available data source
        options = "-csv", "-db"
        args = list(arg.lower() for arg in str(line).split())

        try:
            # Check if the input data source is available in this program or not
            if args[0] not in options:
                raise ValueError("The data source is not available")
            else:
                # Code for initialise CSV data source
                if args[0] == "-csv":
                    try:
                        if len(args) == 1:
                            self._std.select_source(args[0][1:], "employeeInfo.csv")
                            View.warning("No CSV file path specified. A default file \"employee.csv\ will be used.")
                        elif len(args) == 2:
                            self._std.select_source(args[0][1:], args[1])
                        elif len(args) == 3:
                            if args[1] == "-a":
                                self._std.select_source(args[0][1:], args[2], True)
                    except (CSVError, OSError) as e:
                        View.error(e)
                    except Exception as e:
                        View.error(e)
                    else:
                        View.Success("Daa source CSV is selected.")

                # Code for initialize database source
                elif args[0] == "-db":
                    try:
                        self._std.select_source(args[0][1:])
                    except (ConnectionAbortedError, TypeError) as e:
                        View.error(e)
                    except Exception as e:
                        View.error(e)
                    else:
                        View.Success("Data source Database is selected.")

                # Code for initialixe XXXX data source
                else:
                    pass
        #Catch and display error message
        except ValueError as e:
            View.error(str(e) + "\n")
            View.help_select()
        except Exception as e:
            View.error(e)

    def do_add(self, line):
        """
        Add anew entry of data
        :param self:
        :param line:
        :return:
        """
        # Split the input argument to obtain the data
        raw_data = list(arg.lower() for arg in str(line).split())

        try:
            # Check if input data has 7 data fields
            if not len(raw_data) == len(Employee):
                raise AttributeError("Please input correct data.")
            else:
                # Check and wash data by check_all() of DataValidator
                result = self._valid.check_all(raw_data)
                # Check if there is any None which stands for invalid input
                if None in result:
                    key = 0
                    # build a list of name list
                    items = list(map(lambda i: i.name, Employee))
                    e_str = ""
                    while key < len(result):
                        if result[key] is None:
                            # Left alignment
                            e_str += "{:<10}".format(items[key])
                        key += 1
                    raise ValueError("The following field(s) is invalid:\n%s" % e_str)
                else:
                    self._std.add_data(result)
        except (AttributeError, ValueError) as e:
            View.error(str(e) + "\n")
            View.help_add()
        except CSVError as e:
            View.error(e)
        except Exception as e:
            View.error(e)
        else:
            View.success("Add data")

    def do_save(self, arg):
        """
        Save data to specified data source
        :param self:
        :param arg:
        :return:
        """
        # If data source selected, prompt user to do so.
        try:
            self._std.save_data()
        except ValueError as e:
            View.Info(e)
        except (OSError, AttributeError) as e:
            View.error(e)
        except Exception as e:
            View.error(e)
        else:
            View.success("Data is saved.")

    def do_show(self, line):
        """
        Get all instructions
        :param self:
        :param line:
        :return:
        """
        args = list(arg.lower() for arg in str(line).split())
        # Those commands are required single arguments
        # single_commands = ["-a"]
        # Those commands are required two arguments

        plot_commands = ["-p", "-b", "-c"]

        # Show data_table
        if args[0] == "-t":
            if len(self._std.emp_data) == 0 and len(self._std.new_emp_data) == 0:
               View.info("No data to be displayed.")
            if not len(self._std.emp_data) == 0:
                View.display("ORIGINAL DATA:")
                View.display_data(self._std.emp_data, ind=True)
            if not len(self._std.new_emp_data) == 0:
                View.display("\nNew DATA:")
                View.display_data(self._std.new_emp_data, ind=True)
                View.display("\n(Input command \"save\" to save the new data")

        elif args[0] in plot_commands:
            try:
                if len(args) == 1:
                    raise IndexError("Incomplete command line.")

                if args[0] == "-p":
                    self.show_pie(args[1])
                if args[0] == "-b":
                    self.show_bar(args[1])
                if args[0] == "-c":
                    self.show_scatter(args[1])

            except IndexError as e:
                View.error(str(e) + "\n")
                View.help_show()
        else:
            View.info("Invalid command line.\n")
            View.help_show()

    def show_pie(self, line):
        """
        Show Pie chart
        :param self:
        :param line:
        :return:
        """
        try:
            if len(self._std.get_gender()) == 0 or len(self._std.get_bmi()) == 0:
                raise ValueError("No data to display.")
            # Draw gender
            if line.upper() == Employee.GENDER.name:
                View.plot_pie(self._std.get_gender(), "Gender Distribution")
            # Draw BMI
            if line.upper() == Employee.BMI.name:
                View.plot_pie(self._std.get_bmi(), "Body Mass Index (BMI)")
        except ValueError as e:
            View.info(e)
        except Exception as e:
            View.error(e)

    def show_bar(self, line):
        """
        Draw Bar Chart
        :param self:
        :param line:
        :return:
        """
        try:
            if len(self._std.get_gender()) == 0 or len(self._std.get_gender()) == 0:
                raise ValueError("No data to display.")
            # Draw gender
            if line.upper() == Employee.GENDER.name:
                View.plot_bar(self._std.get_bmi(), "Body Mass Index (BMI)")
        except ValueError as e:
            View.info(e)
        except Exception as e:
            View.error(e)

    def show_scatter(Self, line):
        """
        Draw Scatter Chart
        :param Self:
        :param line:
        :return:
        """
        try:
            if len (self._std.get_gender ()) == 0 or len (self._std.get_gender ()) == 0:
                raise ValueError ("No data to display.")
            # Draw gender
            if line.upper () == Employee.GENDER.name:
                View.plot_bar (self._std.get_gender (), "Gender Distribution")
            # Draw BMI
            if line.upper () == Employee.SALARY.name:
                View.plot_bar (self._std.get_salary (), "Body Mass Index (SALARY)")
        except ValueError as e:
            View.info (e)
        except Exception as e:
            View.error (e)

    @staticmethod
    def help_show():
        View.help_show()

    @staticmethod
    def help_add():
        View.help_add()

    @staticmethod
    def help_save():
        View.help_save()

    @staticmethod
    def help_select():
        View.help_select()

    @staticmethod
    def help_quit():
        View.help_quit()

    def do_quit(self, line):
        arg = str(line).lower()
        if not arg == "-f" and not len(self._std.new_data) == 0:
            View.warning("The new data hasn't been saved. En ter \"quit -f\" to quit without saving.")
        else:
            View.display("Thanks for using Console. Bye!")
            return True


if __name__ == "__main__":
    ctl = CLI()
    ctl.cmdloop()

