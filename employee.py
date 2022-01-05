# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Program to be modified in exercise 9.1

# The class represents an employee of some company

class Employee:
    BASE_BONUS = 300

    # The method initializes a new employee object
    # The name, id and starting salary of the employee
    # are given as parameters
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__id = employee_id
        self.__salary = salary
        self.__bonus = 0

    # The method returns the name of the employee
    def get_name(self):
        return self.__name

    # The method returns the id of the employee
    def get_id(self):
        return self.__id

    # The method returns the salary of the employee
    def get_salary(self):
        return self.__salary

    # The method returns the bonus of the employee
    def get_bonus(self):
        return self.__bonus

    # The method changes the salary of the employee
    def change_salary(self, new_salary):
        if new_salary - self.__salary > 200:
            self.__salary = self.__salary + 200
        elif self.__salary - new_salary > 100:
            self.__salary = self.__salary - 100
        else:
            self.__salary = new_salary

    # The method calculates and sets the bonus of the employee based on
    # The constant BASE_BONUS and the bonus coefficient given
    # as a parameter
    def calculate_and_set_bonus(self, bonus_coefficient):
        bonus = bonus_coefficient * Employee.BASE_BONUS
        if 0.5 <= bonus_coefficient <= 2.0:
            self.__bonus = bonus
        else:
            self.__bonus = self.__bonus

    # The method returns a string representation of the information
    # of the employee
    def __str__(self):
        info = "{:s} (employee id: {:d})\n".format(self.__name, self.__id)
        info += "Salary: {:.2f}\n".format(self.__salary)
        info += "Bonus: {:.2f}\n".format(self.__bonus)
        return info
