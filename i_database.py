# Create exceptional error handling interface class
# This is an interface class of Database base class


class IDatabase(object):

    @property
    def create_database_connection(self, database_name='mydb'):
        raise NotImplementedError("An Abstract method has not been implemented yet!")

    def insert_employee_data(self, employee_ob):
        raise NotImplementedError("An Abstract method has not been implemented Yet!!")

    def select_employee_data(self, employee_ob ):
        raise NotImplementedError("An Abstract method has not been implemented yet!!!")
