# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Given class for Exercise 9.2: Coffee containers

class LiquidContainer:

    def __init__(self, description, volume, has_lid):
        "Initializes a new container"
        self.__name = description  # string, the name of the container
        self.__total_volume = volume  # float, the volume of the container in litres
        self.__current_liquid_volume = 0.0  # float, how much liquid is inside the container at the moment
        self.__lid = has_lid  # boolean, whether the container has a lid or not

    def get_name(self):
        return self.__name

    def get_total_volume(self):
        return self.__total_volume

    def get_liquid_volume(self):
        return self.__current_liquid_volume

    def has_lid(self):
        return self.__lid

    def get_available_volume(self):
        "Returns the volume that can still be poured in the container without overflowing."
        return self.__total_volume - self.__current_liquid_volume

    def get_fill_percentage(self):
        "Returns a percentage representing how full the container is."
        return self.__current_liquid_volume / self.__total_volume * 100

    def fill(self):
        self.__current_liquid_volume = self.get_total_volume()

    def flip(self):
        "Flips the container (attempts to empty it to the floor)."
        if not self.has_lid():
            self.__current_liquid_volume = 0.0

    def detach_lid(self):
        self.__lid = False

    def force_flip(self):
        if self.has_lid():
            self.detach_lid()
        self.flip()

    def pour_out(self, amount):
        """
        Attempts to pour [amount] litres of liquid out of the container.
        Returns the amount really poured out.
        """
        amount_to_be_poured = min(self.get_liquid_volume(), amount)
        self.__current_liquid_volume -= amount_to_be_poured
        return amount_to_be_poured

    def pour_in(self, amount):
        """
        Attempts to pour [amount] litres of liquid into the container.
        Returns the amount really poured in.
        """
        amount_to_be_poured = min(self.get_available_volume(), amount)
        self.__current_liquid_volume += amount_to_be_poured
        return amount_to_be_poured

    def pour_to_another(self, other_container, amount):
        """
        Attempts to pour [amount] litres of liquid to [other_container]
        Returns the amount really poured.
        """
        amount_poured_out_of_self = self.pour_out(amount)
        amount_poured_into_the_other = other_container.pour_in(amount_poured_out_of_self)
        # the amount that did not fit the other container:
        amount_poured_back_into_self = self.pour_in(amount_poured_out_of_self - amount_poured_into_the_other)
        return amount_poured_into_the_other

    def empty_to(self, other_container):
        """
        Attempts to pour all the available liquid to other container (from self).
        Returns the amount poured.
        """
        return self.pour_to_another(other_container, self.get_liquid_volume())

    def fill_from(self, other_container):
        """
        Attempts to pour all the available liquid from other container (to self).
        Returns the amount poured.
        """
        return other_container.empty_to(self)

    def __str__(self):
        if self.has_lid():
            lid_string = " (lidded)"
        else:
            lid_string = ''
        return "{:s}{:s} - Filled {:.2f} out of {:.2f} litres ({:.0f}%)".format(
            self.get_name(),
            lid_string,
            self.get_liquid_volume(),
            self.get_total_volume(),
            self.get_fill_percentage()
        )

