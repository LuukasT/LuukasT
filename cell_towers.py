import math

def is_inside_cell_tower_range(point, cell_tower_list):
    loytyyko = False
    for cell_tower in cell_tower_list:
        point[0] = int(point[0])
        cell_tower[0][0] = int(cell_tower[0][0])
        point[1] = int(point[1])
        cell_tower[0][1] = int(cell_tower[0][1])
        etaisyys = ((point[0] - cell_tower[0][0]) ** 2 + (point[1] - cell_tower[0][1]) ** 2)
        etaisyys = math.sqrt(etaisyys)
        if etaisyys <= cell_tower[1]:
            loytyyko = True

    return loytyyko

def find_nearest_tower_in_range(point, cell_tower_list):
    best_tower = float('inf')
    strongest_signal = [-1, -1]
    for cell_tower in cell_tower_list:

        etaisyys = ((point[0] - cell_tower[0][0]) ** 2 + (point[1] - cell_tower[0][1]) ** 2)
        etaisyys = math.sqrt(etaisyys)
        if etaisyys <= cell_tower[1]:
            if etaisyys < best_tower:
                best_tower = etaisyys
                strongest_signal = cell_tower[0]

    return strongest_signal

def coordinates_int(coordinates):
    try:
        coordinates[0] = int(coordinates[0])
        coordinates[1] = int(coordinates[1])
        return coordinates, True
    except ValueError:
        print("Invalid coordinates! Enter the coordinates as integers.")
        return coordinates, False

def main():
    name = input("Enter the name of the file containing the cell tower information:\n")
    ei_toimi = True
    try:
        cell_tower_file = open(name, "r")
        ei_toimi = False
        cell_tower_file.readline()
        cell_tower_list = []
        for rivi in cell_tower_file:
            rivi = rivi.rstrip()
            osa = rivi.split(":")
            if len(osa) != 2:
                print("Invalid line:", rivi)
            else:
                koordinaatit = osa[0]
                toimivuus = osa[1]
                splitted_koordinaatit = koordinaatit.split(",")
                if len(splitted_koordinaatit) != 2:
                    print("Invalid coordinates or radius in line:", rivi)
                else:
                    try:
                        koordinaatti1 = int(splitted_koordinaatit[0])
                        koordinaatti2 = int(splitted_koordinaatit[1])
                        etaisyys = int(osa[1])
                        cell_tower_list.append([[koordinaatti1, koordinaatti2], etaisyys])
                    except ValueError:
                        print("Invalid coordinates or radius in line:", rivi)

        if len(cell_tower_list) == 0:
            ei_toimi = True
            print("File read.\n")
        else:
            print("File read.\n")
            print("Enter coordinates. Stop with an empty line.")
            coordinates = input("Enter the coordinates separated by comma:\n")

            while coordinates != "":
                coordinates = coordinates.split(",")
                if len(coordinates) != 2:
                    print("Invalid coordinates! Enter two coordinates separated by comma.")
                else:
                    test_coordinates = False
                    coordinates, test_coordinates = coordinates_int(coordinates)

                    if test_coordinates:
                        if coordinates[0] < 0 or coordinates[1] < 0:
                            print("Invalid coordinates! Coordinates must be positive integers.")
                        else:
                            loytyyko = False
                            loytyyko = is_inside_cell_tower_range(coordinates, cell_tower_list)
                            if loytyyko:
                                print("The place is inside a cellular network range.")
                                strongest_signal = find_nearest_tower_in_range(coordinates, cell_tower_list)
                                print("The coordinates of the cell tower with the strongest signal: ({:d}, {:d})\n".format(strongest_signal[0], strongest_signal[1]))

                            else:
                                print("The place is not inside of any cell tower range.\n")

                coordinates = input("Enter the coordinates separated by comma:\n")

    except OSError:
        print("Error in reading the file '{:s}'.\n".format(name))

    if ei_toimi:
        print("No cell tower information available.")

    print("Program ends.")

main()
