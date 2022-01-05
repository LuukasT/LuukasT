# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Program to be run in exercise 9.1

from employee import Employee
import random


def main():
    seed = int(input("Enter a seed to initialize the random number generator:\n"))
    random.seed(seed)
    name = input("Enter the name of the first employee:\n")
    salary = int(input("Enter the salary for {:s}:\n".format(name)))
    employee_id = random.randint(100000, 999999)
    employee1 = Employee(name, employee_id, salary)

    name = input("Enter the name of the second employee:\n")
    salary = int(input("Enter the salary for {:s}:\n".format(name)))
    employee_id = random.randint(100000, 999999)
    employee2 = Employee(name, employee_id, salary)

    print("Updating salaries.")
    salary_change = int(input("Enter the new salary for employee {:s}:\n".format(employee1.get_name())))
    employee1.change_salary(salary_change)
    salary_change = int(input("Enter the new salary for employee {:s}:\n".format(employee2.get_name())))
    employee2.change_salary(salary_change)

    print("Time for Christmas bonuses!")
    bonus_coeff = float(input("Enter the bonus coefficient for employee {:s}:\n".format(employee1.get_name())))
    employee1.calculate_and_set_bonus(bonus_coeff)
    bonus_coeff = float(input("Enter the bonus coefficient for employee {:s}:\n".format(employee2.get_name())))
    employee2.calculate_and_set_bonus(bonus_coeff)

    print("Printing the information of the employees at the end.")
    print()
    print(employee1)
    print(employee2)


main()