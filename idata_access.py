from abc import ABCMeta, abstractmethod


class IDataAccess(metaclass=ABCMeta):
    """
    Interface for data access implementation
    :Author: Vaishali Patel
    """
    @abstractmethod
    def read(self):
        """
        Read data from local files or databases
        :return: list of existed Data
        """
        pass

    @abstractmethod
    def save(self, data: list):
        """
        Save data to local files or database
        :return: Boolean
        """
        pass

