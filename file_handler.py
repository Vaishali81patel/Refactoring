import csv
from os import path, makedirs
from IDatabase import *
from employee import Employee


class FileHandler(IDatabase):
    """
        This class enable to handle csv file, read and write
        Written By: Vaishali Patel
    """
    # CSV file_path
    __path = None
    __file_path = None
    __file_name = None
    __field_name = None
    # the header of employee data field in the CSV file.

    def __init__(self, file_path, create = False):
        self.__path = file_path
        paths = str(file_path).split("/")
        if len(paths) > 1:
            self.__file_path = "/".join(paths[0:-1])
        self.__file_name = paths[-1]

        # Initialize fieldnames
        self._fieldnames = list(map(lambda i: i.name, Employee))
        # Create the file if it doesn't exists
        # chdir("./")
        if create:
            self.create_file()

    def create_file(self):
        """
        Create the CSV file at specified path
        :return:
        """
        if self.__file_path is not None and not path.exists(self.__file_path):
            makedirs(self.__file_path)
        # chdir(self.__file_path)
        if not self.file_exist():
            with open(self.__path, "w+") as f:
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(list(e.name for e in Employee))
        else:
            raise OSError("Can't create the file. The file already exists:")

    def read(self):
        """
        This function enable to return content of the CSV file
        :return:
        written By: Vaishali Patel
        """
        # Try to open the file for read. Newline to avoid















