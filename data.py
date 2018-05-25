from enum import Enum, unique


@unique
class Data(Enum):
    """
    Enum for data
    :Author: Vaishali Patel
    """
    EMPID = 0
    GENDER = 1
    AGE = 2
    SALES = 3
    BMI = 4
    SALARY = 5
    BIRTHDAY = 6

   def setData(self, Data):
        self.Data = Data

    def getData(self):
        return self.Data

    def setEmpID(self, EMPID):
       self.__EMPID = EMPID

    def setGENDER(self, GENDER):
        self.__GENDER = GENDER

    def setAGE(self, AGE):
        self.__AGE = AGE

    def setSALES(self, SALES):
        self.__SALES = SALES

    def setBMI(self, BMI):
        self.__BMI = BMI

    def setSALARY(self, SALARY):
        self.__SALARY = SALARY

    def setBIRTHDAY(self, BIRTHDAY):
        self.__BIRTHDAY = BIRTHDAY

    def getEMPID(self):
        return self.EMPID

    def getGENDER(self):
        return self.GENDER

    def getAGE(self):
        return self.AGE

    def getSALES(self):
        return self.SALES

    def getBMI(self):
        return self.BMI

    def getSALARY(self):
        return self.SALARY

    def getBIRTHDAY(self):
        return self.BIRTHDAY

