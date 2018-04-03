from idata_access import IDataAccess
import sqlite3
from employee import Employee
# This class enable to handle database and csv file connection
#
# Author: Patel


class Database(IDataAccess):

    def __init__(self):
        # Create an connection object to connect to Employee Database
        self.db_conn = None
        # Create a "cursor" variable and cursor object
        # in order to execute the sql command
        self.cursor = None
        self.create_db_connection("employeeinfo")

    def create_db_connection(self, database_name='mydb'):
        #
        # This function enable to handle database connection
        # Raise runtime error and type error if unable to connect database
        #
        # Author: Patel
        #
        try:
            self.db_conn = sqlite3.connect(database_name)
            # Try to connect the employee database
            self.cursor = self.db_conn.cursor()
            # Try to execute the connection with the employee database
            self.create_employee_table()
            # try to create the employee table
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (error)

    def create_employee_table(self):
        # This function is enable to create employee table
        # Raise runtime error and type error if unable to create employee table
        #
        # Author: Patel
        #
        # Create employee table if not exists
        try:
            create_table = """ CREATE TABLE IF NOT EXISTS EMPLOYEE ({0} VARCHAR (6), 
                                {1} CHAR, {2} INTEGER, {3} INTEGER, 
                                {4} VARCHAR, {5} INTEGER, {6} DATE);"""
            create_table = self.format_column(create_table)
            self.cursor.execute(create_table)
            self.db_conn.commit()
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (TypeError)

    def format_column(self, sql):
        return sql.format(Employee.EMPID.name,
                          Employee.GENDER.name,
                          Employee.AGE.name,
                          Employee.SALES.name,
                          Employee.BMI.name,
                          Employee.SALARY.name,
                          Employee.BIRTHDAY.name)

    def insert_employee_data(self, row_data):
        # This is function is enable to insert data into employee table
        # raise runtime error and type error if unable to insert data
        #
        # Author: Patel
        #
        #
        try:
            insert_string_1 = "INSERT INTO EMPLOYEE ({0}, {1}, {2}, {3}, {4}, {5}, {6})"
            insert_string_2 = self.format_column(insert_string_1)
            insert_string_2 += """VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}");"""
            try:
                insert_values = insert_string_2.format(row_data[Employee.EMPID.name],
                                                       row_data[Employee.GENDER.name],
                                                       row_data[Employee.AGE.name],
                                                       row_data[Employee.SALES.name],
                                                       row_data[Employee.BMI.name],
                                                       row_data[Employee.SALARY.name],
                                                       row_data[Employee.BIRTHDAY.name])
                self.cursor.execute(insert_values)
                self.db_conn.commit()
            except ConnectionError:
                print(ConnectionError)
            except TypeError as error:
                print(TypeError)
                return False

        except AttributeError as err:
            print (err)
            return False
        except UnboundLocalError as err:
            print (err)
            return False
        except TypeError as err:
            print (err)
            return False
        return True

    def save(self, employee):
        #
        # This function is unable to \
        # save employee data into employee.db
        # Raise runtime error and type error \
        # if unable to retrieve database file
        #
        # Author: Patel
        #
        for e in employee:
            self.insert_employee_data(e)

    def read(self):
        # This function is unable to retrieve \
        # data_arr_list from employee table
        # Raise runtime error and type error \
        # if unable to retrieve data from employee table
        #
        # Author: Patel
        #
        data_arr_list = []  # Retrieve employee data in dara_arr list format
        try:
            self.cursor.execute(" SELECT * FROM EMPLOYEE ")
            result = self.cursor.fetchall()
            for r in result:
                    data_arr_list.append({e.name :r[e.value] for e in Employee})
            return data_arr_list
        except ConnectionError:
            print(ConnectionError)
        except AttributeError as err:
            print(err)
            return False


