def calculate_consumption(size, residents):
    basic_consumption = 2206
    residentcosumption = 0
    if size <= 30 and residents == 1:
        sizeconsumption = 0
    elif 110 >= size > 30:
        sizeconsumption = (((size // 10) - 2) * 0.16)
    elif size > 110:
        sizeconsumption = (8 * 0.16) + (((size // 10) - 10) * 0.05)
    if residents > 1:
        if residents <= 3:
            residentconsumption = (residents - 1) * 0.12
        elif residents > 3:
            residentconsumption = (2 * 0.12) + (residents - 3) * 0.07
    else:
        residentconsumption = 0
    consumption = (sizeconsumption + residentconsumption + 1) * 2206.0

    return consumption
    pass
def find_cheapest_contract(contracts, consumption):
    cheapest_contract = ["ABC", float('inf')]
    for rivi in contracts:
        hinta = ((contracts[rivi]["kWh_price"]) * consumption) / 100 + (contracts[rivi]["month_price"]) * 12
        if hinta < cheapest_contract[1]:
            cheapest_contract[0] = rivi
            cheapest_contract[1] = hinta

    return cheapest_contract[0], cheapest_contract[1]

def find_ecofriendly_contract(contracts, consumption):
    ecofriendly_contract = ["ABC", 0, 0]
    for rivi in contracts:
        hinta = ((contracts[rivi]["kWh_price"]) * consumption) / 100 + (contracts[rivi]["month_price"]) * 12
        if ecofriendly_contract[1] < (contracts[rivi]["renewable"]):
            ecofriendly_contract[0] = rivi
            ecofriendly_contract[1] = (contracts[rivi]["renewable"])
            ecofriendly_contract[2] = hinta
        elif ecofriendly_contract[1] == (contracts[rivi]["renewable"]):
            if ecofriendly_contract[2] > (((contracts[rivi]["kWh_price"]) * consumption) / 100 + (contracts[rivi]["month_price"]) * 12):
                ecofriendly_contract[2] = (((contracts[rivi]["kWh_price"]) * consumption) / 100 + (contracts[rivi]["month_price"]) * 12)
                ecofriendly_contract[0] = rivi
    return ecofriendly_contract[0], ecofriendly_contract[2]

def print_all_contracts(contracts):

    for rivi in contracts:
        print(rivi)
        print("   kWh_price: {:.2f}".format(contracts[rivi]["kWh_price"]))
        print("   month_price: {:.2f}".format(contracts[rivi]["month_price"]))
        print("   renewable: {:.2f}".format(contracts[rivi]["renewable"]))


def main():
    nimi = input("Enter the file name.\n")
    loytyi = False
    try:
        sopimustiedosto = open(nimi, "r")
        sopimustiedosto.readline()
        contracts = {}
        loytyi = True
        for rivi in sopimustiedosto:
            rivi = rivi.rstrip()
            osat = rivi.split(",")
            if len(osat) == 4:
                try:
                    osat[0] = str(osat[0])
                    osat[1] = float(osat[1])
                    osat[2] = float(osat[2])
                    osat[3] = float(osat[3])
                    contracts[osat[0]] = {"kWh_price" : osat[1], "month_price": osat[2], "renewable": (osat[3] / 100)}

                except ValueError:
                    print("Invalid value: {:s}".format(rivi))
            elif len(rivi) != 0:
                print("Invalid line: {:s}".format(rivi))

    except OSError:
        print("Error while reading the file. Program ends.")
    if loytyi:
        print("")
        size = int(input("Enter the size of your apartment (m2).\n"))
        residents = int(input("Enter the number of residents.\n"))
        estimate = int(input("Enter an estimate of your annual electricity consumption (kWh).\n"))
        print("")
        print_all_contracts(contracts)
        print("")
        consumption = calculate_consumption(size, residents)
        cheapest_contract, cheapest_contract_cost = find_cheapest_contract(contracts, consumption)
        cheapest_contract_est, cheapest_contract_cost_est = find_cheapest_contract(contracts, estimate)
        ecofriendly_contract, ecofriendly_contract_cost = find_ecofriendly_contract(contracts, consumption)
        ecofriendly_contract_est, ecofriendly_contract_cost_est = find_ecofriendly_contract(contracts, estimate)
        if cheapest_contract != ecofriendly_contract:
            print("The best deals according to the calculated consumption ({:.0f} kwh):".format(consumption))
            print("The cheapest contract is {:s} and costs {:.2f} eur/year.".format(cheapest_contract, cheapest_contract_cost))
            print("The most eco-friendly contract is {:s} and costs {:.2f} eur/year.\n".format(ecofriendly_contract, ecofriendly_contract_cost))
        else:
            print("The best deals according to the calculated consumption ({:.0f} kwh):".format(consumption))
            print("The cheapest contract is also the most eco-friendly and it is\n{:s} and costs {:.2f} eur/year.".format(ecofriendly_contract, ecofriendly_contract_cost))
        if cheapest_contract_est != ecofriendly_contract_est:
            print("The best deals according to the user estimated consumption ({:.0f} kwh):".format(estimate))
            print("The cheapest contract is {:s} and costs {:.2f} eur/year.".format(cheapest_contract_est, cheapest_contract_cost_est))
            print("The most eco-friendly contract is {:s} and costs {:.2f} eur/year.\n".format(ecofriendly_contract_est, ecofriendly_contract_cost_est))
        else:
            print("The best deals according to the user estimated consumption ({:.0f} kwh):".format(estimate))
            print("The cheapest contract is also the most eco-friendly and it is\n{:s} and costs {:.2f} eur/year.".format(ecofriendly_contract_est, ecofriendly_contract_cost_est))


main()
