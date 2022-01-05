#Luukas Tuori

class RentApartment:
    RENTAL_SERVICE_FEE = 100  # eur per month
    STUDIO_SIZE_LIMIT = 32  # m2
    ONE_BEDROOOM_SIZE_LIMIT = 45  # m2
    STUDIO_PRICE_LEVEL = 25  # eur/m2
    ONE_BEDROOOM_PRICE_LEVEL = 20  # eur/m2
    LARGE_PRICE_LEVEL = 18  # eur/m2
    TRANSFER_TAX = 0.02

    def __init__(self, address, rent, maintenance_charge, size, free_of_debt_price,):
        self.__address = address
        self.__rent = rent
        self.__maintenance_charge = maintenance_charge
        self.__size = size
        self.__free_of_debt_price = free_of_debt_price
        self.__rental_service = False
        self.__renovation_costs = 0

    def get_address(self):
        return self.__address

    def get_rent(self):
        return self.__rent

    def get_maintenance_charge(self):
        return self.__maintenance_charge

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__free_of_debt_price

    def get_renovation_costs(self):
        return self.__renovation_costs

    def update_rental_service(self):
        if self.__rental_service == False:
            self.__rental_service = True
        else:
            self.__rental_service = False
        return self.__rental_service

    def increase_rent(self, new_rent):
        if new_rent > self.__rent:
            self.__rent = new_rent
            return True
        else:
            return False


    def add_renovation_costs(self, costs):
        self.__renovation_costs = self.__renovation_costs + costs

    def calculate_square_meter_rent(self):
        return self.__rent / self.__size

    def calculate_rental_income(self):
        if self.__rental_service == True:
            return ((self.__rent - RentApartment.RENTAL_SERVICE_FEE - self.__maintenance_charge)\
            * 12 / (self.__free_of_debt_price +
            self.__free_of_debt_price * RentApartment.TRANSFER_TAX +
            self.__renovation_costs)) * 100
        else:
            return ((self.__rent - self.__maintenance_charge)\
            * 12 / (self.__free_of_debt_price +
            self.__free_of_debt_price * RentApartment.TRANSFER_TAX +
            self.__renovation_costs)) * 100

    def compare_rental_incomes(self, other):
        if RentApartment.calculate_rental_income(self) > RentApartment.calculate_rental_income(other):
            return 1
        elif RentApartment.calculate_rental_income(self) == RentApartment.calculate_rental_income(other):
            return 0
        else:
            return -1

    def calculate_return_on_equity(self, down_payment, loan_interest):
        if self.__rental_service == True:
            return (((self.__rent - RentApartment.RENTAL_SERVICE_FEE - self.__maintenance_charge
                      - loan_interest) * 12) / down_payment) * 100
        else:
            return (((self.__rent - self.__maintenance_charge
                      - loan_interest) * 12) / down_payment) * 100

    def check_price_level(self):
        enough = False
        if self.__size < 32:
            if RentApartment.calculate_square_meter_rent(self) >= 25:
                enough = True
            else:
                enough = False
        elif 32 <= self.__size < 45:
            if RentApartment.calculate_square_meter_rent(self) >= 20:
                enough = True
            else:
                enough = False
        elif 45 <= self.__size:
            if RentApartment.calculate_square_meter_rent(self) >= 18:
                enough = True
            else:
                enough = False
        return enough

    def __str__(self):
        if self.__rental_service == True:
            service = "in use"
        else:
            service = "not in use"
        return "Address: " + self.__address + "\n" +\
                "Maintenance charge: " + str(self.__maintenance_charge) + " eur" + "\n" +\
                "Size: " + str(self.__size) + " m2" + "\n" +\
                "Rent: " + str(self.__rent) + " eur" + "\n" +\
                "Rental service: " + service
