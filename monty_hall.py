import random


def initialize_doors(number_of_doors):
    doors = [False] * number_of_doors
    car = random.randint(0, number_of_doors - 1)
    doors[car] = True
    return doors

def remove_wrong_doors(chosen_door, doors):
    if doors[chosen_door - 1]:
        false_door = random.randint(1, len(doors))
        while false_door == chosen_door:
            false_door = random.randint(1, len(doors))
        return false_door
    else:
        for i in range(0, len(doors)):
            if doors[i] == True:
                return i + 1

def print_doors(doors, dont_open):
    print(" _  " * len(doors))
    for i in range(0, len(doors)):
        if i + 1 in dont_open:
            print("| | ", end="")
        else:
            if doors[i]:
                print("|C| ", end="")
            else:
                print("|G| ", end="")
    print("")
    print("|_| " * len(doors))
    for i in range(0, len(doors)):
        print("{:^3d} ". format(i + 1), end="")
    print("")



def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)

    number_of_doors = int(input("How many doors?\n"))
    while 3 > number_of_doors or number_of_doors > 999:
        print("The number of doors must be between 3-999!")
        number_of_doors = int(input("How many doors?\n"))

    doors = initialize_doors(number_of_doors)

    dont_open = range(1, len(doors) + 1)
    print_doors(doors, dont_open)

    chosen_door = int(input("Choose a door 1-{:d}.\n".format(len(doors))))
    while 1 > chosen_door or chosen_door > len(doors):
        chosen_door = int(input("Choose a door 1-{:d}.\n".format(len(doors))))
    print("You chose the door number {:d}.".format(chosen_door))
    dont_open = remove_wrong_doors(chosen_door, doors)

    print("...")
    print_doors(doors, [chosen_door, dont_open])
    doors_opened = len(doors) - 2
    print(doors_opened, "certainly wrong doors were opened. The door number", dont_open, "was left.")
    chosen_door1 = int(input("Choose {:d} if you want to keep the door you first chose and choose {:d} if you want to change the door.\n".format(chosen_door, dont_open)))

    while chosen_door1 != chosen_door and chosen_door1 != dont_open:
        chosen_door1 = int(input("Choose {:d} if you want to keep the door you first chose and choose {:d} if you want to change the door.\n".format(chosen_door, dont_open)))
    print_doors(doors, [])
    if doors[chosen_door1 - 1] == True:
        print("Congratulations! The car was behind the door you chose!")
    else:
        print("A goat emerged from the door you chose! The car was behind the other door :(")

main()