# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius, modified by Veera Laine
# Template for Exercise 9.2 Coffee containers

from container import LiquidContainer


def main():
    large = input("Big coffee cup name and volume: ")
    osat = large.split("/")
    name = osat[0]
    volume = float(osat[1])
    has_lid = False
    big_cup = LiquidContainer(name, volume, has_lid)

    Small = input("Small coffee cup name and volume: ")
    osat = Small.split("/")
    name = osat[0]
    volume = float(osat[1])
    has_lid = False
    small_cup = LiquidContainer(name, volume, has_lid)

    jug = input("Coffee jug name and volume: ")
    osat = jug.split("/")
    name = osat[0]
    volume = float(osat[1])
    has_lid = True
    jug = LiquidContainer(name, volume, has_lid)

    print("Created the following containers:")
    print(big_cup)
    print(small_cup)
    print(jug)


    print("\nFilling {}...".format(jug.get_name()))
    print("Jug status after filling:")
    jug.fill()
    print(jug)

    amount_to_be_served = float(input("\nHow many litres of coffee should be served?\n"))
    print("Trying to pour {:g} litres from {:s} into {:s}and {:s}".format(amount_to_be_served, jug.get_name(), big_cup.get_name(), small_cup.get_name()))
    jug.pour_to_another(big_cup, amount_to_be_served)
    jug.pour_to_another(small_cup, amount_to_be_served)
    print("Managed to pour {:g} litres to {:s}".format(big_cup.get_liquid_volume(), big_cup.get_name()))
    print("Managed to pour {:g} litres to {:s}".format(small_cup.get_liquid_volume(), small_cup.get_name()))

    print("\nCup and jug statuses after pouring:")
    print(big_cup)
    print(small_cup)
    print(jug)

    if big_cup.get_liquid_volume() == small_cup.get_liquid_volume():
        print("\nBoth were happy for having the same amount of coffee and lived happily everafter.")
    else:

        print("\nThe holder of {:s} became angry for having less coffee and flipped their coffee cup!".format(small_cup.get_name()))
        small_cup.flip()

        print("\nThey also flipped the jug!")
        jug.flip()

        print("However, it had a lid, so the liquid stayed inside:")
        print(jug)

        print("\nSo they had to force flip to the jug!")
        jug.force_flip()

        print("Now it's empty and no longer has a lid:")
        print(jug)

        print("\nNext they got mad and nicked all the coffee they could from {:s}".format(big_cup.get_name()))

        # Fill the format with the stolen amount
        print("{:g} litres were stolen.".format(big_cup.empty_to(small_cup)))

        print("\nCup statuses after the theft:")
        print(big_cup)
        print(small_cup)

        # Fill the format with the name of the small cup
        print("\nNow finally the holder of {:s} can drink their coffee:".format(small_cup.get_name()))
        small_cup.pour_out(small_cup.get_liquid_volume())

        print(small_cup)


main()

