# Y1 Autumn 2021
# Basic Course in Programming Y1
# Author: Teemu Sirkia and Kerttu Pollari-Malmi. Translated by Veera Laine

# Program to test class RestaurantBill

from restaurant_bill import RestaurantBill


# A helper fuction to read an integer.

def read_integer():
    read_ok = False
    while not read_ok:
        try:
            number = int(input())
            read_ok = True
        except ValueError:
            print("Invalid integer!")
            print("Enter a new value.")
    return number


# A helper function to read a decimal number.

def read_decimal_number():
    read_ok = False
    while not read_ok:
        try:
            number = float(input())
            read_ok = True
            return number
        except ValueError:
            print("Not a decimal number. Enter a new value.")


# The function asks the type of the order (drink or food) and
# adds the enterd price to RestaurantBill object which is given
# as parameter.

def add_item_to_bill(bill):
    print("Do you want to add food or a drink? (1=food, 2=drink)")
    choice = read_integer()
    while choice != 1 and choice != 2:
        print("Do you want to add food or a drink? (1=food, 2=drink)")
        choice = read_integer()
    print("Enter the price to be added.")
    total_sum = read_decimal_number()
    if choice == 1:
        bill.add_to_bill(total_sum, False)
    else:
        bill.add_to_bill(total_sum, True)


# The function asks the price to be corrected and fixes accordingly
# RestaurantBill object that is given as parameter.

def fix_bill(bill):
    print("Do you want to fix the price of a drink or food? (1=food, 2=drink)")
    choice = read_integer()
    while choice != 1 and choice != 2:
        print("Do you want to fix the price of a drink or food? (1=food, 2=drink)")
        choice = read_integer()
    if choice == 1:
        food_prices = bill.get_food_prices()
        print("Saved prices:")
        for i in range(len(food_prices)):
            print("{:2d}. {:7.2f}".format((i + 1), food_prices[i]))
        print("Which line do you want to fix?")
        rivinro = read_integer()
        print("Enter a new price (0.0 = delete line).")
        fixed_price = read_decimal_number()
        if bill.fix_price(rivinro, False, fixed_price):
            print("The bill is fixed successfully.")
        else:
            print("The bill could not fixed as you requested.")
    elif choice == 2:
        drink_prices = bill.get_drink_prices()
        print("Saved prices")
        for i in range(len(drink_prices)):
            print("{:2d}. {:7.2f}".format((i + 1), drink_prices[i]))
        print("Which line do you want to fix?")
        rivinro = read_integer()
        print("Enter a new price (0.0 = delete line).")
        fixed_price = read_decimal_number()
        if bill.fix_price(rivinro, True, fixed_price):
            print("The bill is fixed successfully.")
        else:
            print("The bill could not fixed as you requested.")


# The function prints RestaurantBill object given as parameter.

def print_table(bill):
    print()
    print(bill)
    print()


# The function prints RestaurantBill object given as parameter.

def print_bill(bill):
    print()
    print(bill.make_bill())
    print()


# The function prints all possible actions and reads the number
# of the action entered by the user.

def ask_choice():
    print("Choose action:")
    print("1. Add a dish or drink to the bill of the table")
    print("2. Fix the bill of the table")
    print("3. Print information of the table")
    print("4. Print the bill of the table")
    choice = read_integer()
    return choice


def main():
    print("How many tables are in use in the restaurant?")
    tables = read_integer()
    while tables < 1:
        print("Invalid number of tables. Must be at least one table.")
        print("How many tables are in use in the restaurant?")
        tables = read_integer()

    # The tables of the restaurant are stored in a list. Each element of the list is a RestaurantBill object
    # corresponding to the table number.
    tables_list = []
    for i in range(tables):
        table_waitress = input("Enter the name of waitress for table {:d}.\n". \
                               format(i + 1))
        tables_list.append(RestaurantBill(i + 1,
                                          table_waitress))

    print("Enter the table number or enter 0 to stop.")
    table_number = read_integer()
    while table_number != 0:
        if 1 <= table_number <= tables:
            choice = ask_choice()
            if choice == 1:
                add_item_to_bill(tables_list[table_number - 1])
            elif choice == 2:
                fix_bill(tables_list[table_number - 1])
            elif choice == 3:
                print_table(tables_list[table_number - 1])
            elif choice == 4:
                print_bill(tables_list[table_number - 1])
        print("Enter the table number or enter 0 to stop.")
        table_number = read_integer()


main()

