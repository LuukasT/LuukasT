def main():
    nimi = input("Enter the name of the file containing your exercise diary:\n")
    try:
        urheilutiedosto = open(nimi, "r")
        sport = input("What sport are you interested in?\n")
        summa = 0
        days = 0
        rivit = 0
        print("Day        Time")
        loytyi = False
        for rivi in urheilutiedosto:
            rivi = rivi.rstrip()
            osat = rivi.split(",")
            rivit = rivit + 1
            if osat[1] == sport:
                aika = int(osat[2])
                print("{:s}   {:d} min".format(osat[0], aika))
                days = days + 1
                summa = summa + aika
                loytyi = True
        urheilutiedosto.close()
        if loytyi:
            print("-" * 31)
            tunnit = summa // 60
            minuutit = summa - (tunnit * 60)
            print("Total exercise time: {:.0f} h {:.0f} min".format(tunnit, minuutit))
            print("Number of exercise days:", days)
        else:
            print("The sport '{:s}' was not found in the file.".format(sport))
    except ValueError:
        print("Incorrect time in the file '{:s}'. Program ends.".format(nimi))
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(nimi))


main()

