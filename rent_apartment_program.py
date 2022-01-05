# Y1 AUTUM 2021
# Basic Course in Programming Y1
# Author: Veera Laine
# Test program for class RentApartment

from rent_apartment import RentApartment


def menu():
    print()
    print("Choose an action")
    print("1. Apartment is ready to be rented")
    print("2. Add renovation costs")
    print("3. Increase rent")
    print("4. Check price level")
    print("5. Use rental service (100 e/month) / Remove rental service")
    choice = int(input())
    print()
    return choice


def main():
    apartment1 = RentApartment("Munkkivuori 1C 3", 950, 300, 52, 450000)  # Create a new RentApartment obeject
    print("You have one rental apartment which is")
    print(apartment1)
    print("\nLet's add the information of your second rental apartment.\n")

    address = input("Enter the address of the house.\n")
    maintenance_charge = float(input("Enter the maintenance charge.\n"))
    size = float(input("Enter the size of the apartment.\n"))
    loan = float(input("Enter the loan amount.\n"))
    rent = float(input("Enter the rent of the apartment.\n"))
    apartment2 = RentApartment(address, rent, maintenance_charge, size, loan)  # Create another RentApartment obeject
    print()
    print("Is your apartment {:s} ready to rent?\n".format(apartment2.get_address()))
    action = menu()
    while (action != 1):
        if action == 2:
            renovation = float(input("Enter the renovation costs.\n"))
            apartment2.add_renovation_costs(renovation)
        elif action == 3:
            new_rent = float(input("Enter the new rent.\n"))
            rent_increace_ok = apartment2.increase_rent(new_rent)
            if rent_increace_ok:
                print("Rent has been increased succesfully")
            else:
                print("The increase failed.")
                print("The new rent is less than the current rent which is {:.2f} euros".format(apartment2.get_rent()))
        elif action == 4:
            price_level = apartment2.check_price_level()
            if price_level:
                print("The price level of the apartment is high enough.")
            else:
                print("The price level of the apartment is quite low. Should you increase the rent?")
        elif action == 5:
            rental_service = apartment2.update_rental_service()
            if rental_service:
                print("Rental service is now in use.")
            else:
                print("Rental service is not in use.")

        else:
            print("You chose an invalid action.")
        action = menu()
    print("Let's calculate the return on equity of {:s}.".format(apartment2.get_address()))
    invested_capital = float(input("Enter the down payment of {:s}.\n".format(apartment2.get_address())))
    interest = float(input("Enter the interest of the loan (eur/month).\n"))
    apartment2_return_capital = apartment2.calculate_return_on_equity(invested_capital, interest)
    print("The return on equity is {:.1f} percent".format(apartment2_return_capital))

    print("Let's finally compare your apartments rental incomes.")
    better_income = apartment1.compare_rental_incomes(apartment2)
    if better_income == 1:
        print("{:s} has higher rental income.".format(apartment1.get_address()))
    elif better_income == -1:
        print("{:s} has higher rental income.".format(apartment2.get_address()))
    else:
        print("Your apartments rental incomes are equal.".format())


main()
