from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    """
    This is an interface
    """
    @staticmethod
    @abstractmethod
    def display(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def error(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def success(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def display_data(data, ind=False):
        """
        Output data
        :param data: (list)
        :param ind: (Boolean)
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def display_pie_plot(data, title=""):
        """
       Plot a pie chart for gender, BMI
       :param data: data dictionary
       :param title: string
       :return: None
       :Author: Vaishali Patel
       """
        pass

    @staticmethod
    @abstractmethod
    def display_bar_plot(data, title=""):
        """
        Plot a vertical bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def display_bar_horizon(data, title=""):
        """
        Plot a horizontal bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def display_scatter_plot(data, title=""):
        """
        Plot a Scatter bar chart for men vs women
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass
