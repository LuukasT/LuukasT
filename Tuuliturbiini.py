def calculate_powers(velocities_list):
    power_list = []
    for velocity in velocities_list:
        velocity = float(velocity)
        if 3 <= velocity <= 25:
            power = ((8 / 27) * 1.225 * (velocity ** 3) * 8659) / 1000
            power_list.append(power)
        else:
            power_list.append(0.0)
    return power_list

def calculate_capacity_factor(power_list):
    energia = 0
    tunnit = 0
    for power in power_list:
        energia = energia + power
        tunnit = tunnit + 1
    max_teho = 3450 * tunnit
    netto_kap_ker = energia / max_teho

    return netto_kap_ker

def main ():
    nimi = input("Enter the name of the file containing wind velocities.\n")
    try:
        tuulitiedosto = open(nimi, "r")
        tuulitiedosto.readline()
        velocities_list = []
        tunnit = 0
        loytyi = False
        for rivi in tuulitiedosto:
            if len(velocities_list) <= 24:
                rivi = rivi.rstrip()
                osat = rivi.split(",")
                if len(osat) == 6:
                    velocities_list.append(osat[5])
                    tunnit = tunnit + 1
                    loytyi = True

        if loytyi:
            power_list = calculate_powers(velocities_list)
            max_tuuliteho = float(max(power_list))
            print("")
            print("The maximum power of the wind turbine was {:.1f} kW.".format(max_tuuliteho))
            summa = sum(power_list)
            print("The wind turbine generated {:.1f} kWh of electricity.".format(summa))
            netto_kap_ker = float(calculate_capacity_factor(power_list))
            print("The capacity factor of the wind turbine was {:.3f}.".format(netto_kap_ker))
    except OSError:
        print("")
        print("Error while reading the '{:s}' file. Program ends.".format(nimi))

main()
