# Luukas Tuori

class RestaurantBill:
    FOOD_VAT = 14.0
    DRINK_VAT = 24.0

    def __init__(self, table_number, waitress_name):
        self.__table = table_number
        self.__waitress = waitress_name
        self.__food = []
        self.__drinks = []

    def get_table(self):
        return self.__table

    def get_waitress(self):
        return self.__waitress

    def get_food_prices(self):
        return self.__food

    def get_drink_prices(self):
        return self.__drinks

    def add_to_bill(self, price, is_drink):
        if price > 0:
            if is_drink:
                self.__drinks.append(price)
            else:
                self.__food.append(price)

    def fix_price(self, line, is_drink, new_price):
        returned = False
        if new_price > 0:
            if is_drink:
                if len(self.__drinks) >= line - 1 and line >= 1:
                    self.__drinks[line - 1] = new_price
                    returned = True
                else:
                    returned = False
            elif not is_drink:
                if len(self.__food) >= line - 1 and line >= 1:
                    self.__food[line - 1] = new_price
                    returned = True
                else:
                    returned = False
        elif new_price == 0.0:
            if is_drink:
                try:
                    if len(self.__drinks) >= line - 1 and line >= 1:
                        del self.__drinks[line - 1]
                        returned = True
                except IndexError:
                    returned = False
            elif not is_drink:
                try:
                    if len(self.__food) >= line - 1 and line >= 1:
                        del self.__food[line - 1]
                        returned = True
                except IndexError:
                    returned = False
        else:
            returned = False
        return returned

    def calculate_drink_prices(self):
        veroton_summa = 0
        alv_summa = 0
        verollinen_summa = 0
        for drink in self.__drinks:
            veroton_summa = veroton_summa + (drink / (1 + RestaurantBill.DRINK_VAT / 100))
            verollinen_summa = verollinen_summa + drink
        alv_summa = verollinen_summa - veroton_summa
        return veroton_summa, alv_summa, verollinen_summa

    def calculate_food_prices(self):
        veroton_summa = 0
        alv_summa = 0
        verollinen_summa = 0
        for food in self.__food:
            veroton_summa = veroton_summa + (food / (1 + RestaurantBill.FOOD_VAT / 100))
            verollinen_summa = verollinen_summa + food
        alv_summa = verollinen_summa - veroton_summa
        return veroton_summa, alv_summa, verollinen_summa

    def calculate_total(self):
        ruoka_summa = 0
        juoma_summa = 0
        for food in self.__food:
            ruoka_summa = ruoka_summa + food
        for drink in self.__drinks:
            juoma_summa = juoma_summa + drink

        return ruoka_summa + juoma_summa

    def make_bill(self):
        ruoat = ""
        for ruoka in self.__food:
            ruoat = ruoat + "{:16.2f}\n".format(ruoka)
        juomat = ""
        for juoma in self.__drinks:
            juomat = juomat + "{:16.2f}\n".format(juoma)
        veroton_ruoka_summa, alv_ruoka_summa, verollinen_ruoka_summa = RestaurantBill.calculate_food_prices(self)
        veroton_juoma_summa, alv_juoma_summa, verollinen_juoma_summa = RestaurantBill.calculate_drink_prices(self)
        return "Table: {:d}\n".format(self.__table) + \
               "Waitress: {:s}\n".format(self.__waitress) + \
               "FOOD:\n" + \
               ruoat + \
               "DRINKS:\n" + \
               juomat + \
               "------------------------------\n" + \
               "Total {:7.2f}\n".format(RestaurantBill.calculate_total(self)) + \
               "\n" + \
               "           sales     VAT     total\n" + \
               "VAT 24 %: {:7.2f} {:7.2f} {:7.2f}\n".format(veroton_juoma_summa, alv_juoma_summa,
                                                          verollinen_juoma_summa) + \
               "VAT 14 %: {:7.2f} {:7.2f} {:7.2f}".format(veroton_ruoka_summa, alv_ruoka_summa, verollinen_ruoka_summa)

    def __str__(self):
        return "Table: {:d}\n".format(self.__table) + \
               "Waitress: {:s}\n".format(self.__waitress) + \
               "Total sum so far: {:.2f} eur.".format(RestaurantBill.calculate_total(self))
