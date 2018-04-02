from abc import ABCMeta, abstractmethod
# An abstract method is a method that is declared,
# but contains no implementation. Abstract classes
# may not be instantiated, and require subclasses
# to provide implementations for the abstract methods.


class IDatabase(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        """
        This enable to read data from the local files or database
        :return: list of existing Data
        """
        pass

    @abstractmethod
    def save(self, data: list):
        """
        This enable to save data to local files or database
        :param data:
        :return: Boolean
        """
        pass
