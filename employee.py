# Create an employee class


class Employee:

    # Initialize the attribute
    def __init__(self, empid, gender, age, sales, bmi, salary, birthday):
        self.empid = empid
        self.gender = gender
        self.age = age
        self.sales = sales
        self.bmi = bmi
        self.salary = salary
        self.birthday = birthday

    def set_empid(self, empid):
        self.empid = empid

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def set_sales(self, sales):
        self.sales = sales

    def set_bmi(self, bmi):
        self.bmi = bmi

    def set_salary(self, salary):
        self.salary = salary

    def set_birthday(self, birthday):
        self.birthday(self.birthday)

