def sanakirja_berry(BERRY_TYPES, file):
    file.readline()
    marjat = {}
    for rivi in file:
        rivi = rivi.rstrip()
        osa = rivi.split(",")
        if len(osa) != 3 and rivi != "":
            print("Invalid line", rivi)
        elif len(osa) == 3:
            try:
                maara = int(osa[2])
                if osa[1] in BERRY_TYPES:
                    if osa[1] not in marjat:
                        marjat[osa[1]] = maara
                    else:
                        marjat[osa[1]] = marjat[osa[1]] + maara

                else:
                    print("Invalid line:", rivi)
            except ValueError:
                print("Invalid line", rivi)

    return marjat
def sanakirja_price(BERRY_TYPES, file):
    file.readline()
    hinnat = {}
    for rivi in file:
        rivi = rivi.rstrip()
        osa = rivi.split(":")
        if len(osa) != 2 and rivi != "":
            print("Invalid line:", rivi)
        elif len(osa) == 2:
            try:
                hinta = float(osa[1])
                if osa[0] in BERRY_TYPES:
                    hinnat[osa[0]] = hinta
                else:
                    print("Invalid line:", rivi)
            except ValueError:
                print("Invalid line:", rivi)

    return hinnat
def price_finder(marjat, hinnat):
    summa = 0
    for marja in marjat:
        if marja in hinnat:
            summa = summa + 0
        elif marja not in hinnat:
            summa = summa + 1
    return summa
def main():
    BERRY_TYPES = ["blueberry", "lingonberry", "cloudberry", "cranberry", "raspberry", "strawberry"]
    name = 0
    try:
        name = input("Enter the name of the file containing the berry data:\n")
        berryfile = open(name, "r")
        marjat = sanakirja_berry(BERRY_TYPES, berryfile)
        print("File read.")

        name = input("Enter the name of the file containing the prices of the berries:\n")
        pricefile = open(name, "r")
        hinnat = sanakirja_price(BERRY_TYPES, pricefile)
        print("File read.")

        prices_found = price_finder(marjat, hinnat)
        if prices_found == 0:
            print("")
            print("Berry type   Picked berries (kg)   Money earned (eur)")
            print("-" * 53)
            for marja in marjat:
                print("{:12s}{:19d}{:>20.2f}".format(marja, marjat[marja], (marjat[marja] * hinnat[marja])))
            print("-" * 53)
            kilosumma = 0
            rahasumma = 0
            for marja in marjat:
                kilosumma = kilosumma + marjat[marja]
                rahasumma = rahasumma + (marjat[marja] * hinnat[marja])
            print("{:12s}{:19d}{:>20.2f}\n".format("Total", kilosumma, rahasumma))
            print("")

        else:
            print("Some of the berry prices are missing from the file '{:s}'.".format(name))

    except OSError:
        print("Invalid file:", name,)
    print("Program ends.")
main()
