import math
import matplotlib.pyplot as plt

area = [-2, -1, 0, 1, 2]

print("Berechnung einer Wertetabelle für eine quadratische Funktion:")
print()

only_yaxis = input("Scheitelpunkformel? (j/n): ")

if only_yaxis == "n":
    normal_parable = input("Normalparabel? (j/n): ")

    if normal_parable == "j":  
        print("---------------------------------------------------------------")
        for x in [-2, -1, 0, 1, 2]:
            print(x, (x**2))

        print()
        print("Scheitelpunkt: (0|0)")

        plt.plot(area, [((-2)**2), ((-1)**2), (0**2), (1**2), (2**2)])
        plt.show()

    elif normal_parable == "n":
        opentop_opendownwards = input("Nach oben(1) oder unten(2) geöffnet? (1/2): ")
        stretched_compressed_or_not = input("gestreckt oder gestaucht(1) oder normal(2)? (1/2): ")
        move_parable_up_down = input("Nach oben oder unten(1) oder garnicht verschoben(2) (1/2): ")

        if opentop_opendownwards == "1" and stretched_compressed_or_not == "1" and move_parable_up_down == "1":
            stretched_compressed = float(input("Gestreckt oder gestaucht um: "))
            move_parable = float(input("Verschoben um: "))

            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, (stretched_compressed * x**2 + move_parable))
            
            print()
            print("Scheitelpunkt: (0|" + str(move_parable) + ")")

            plt.plot(area, [(stretched_compressed * (-2)**2 + move_parable), (stretched_compressed * (-1)**2 + move_parable), 
                    (stretched_compressed * 0**2 + move_parable), (stretched_compressed * 1**2 + move_parable), (stretched_compressed * 2**2 + move_parable)])
            plt.show()

        elif opentop_opendownwards == "1" and stretched_compressed_or_not == "2" and move_parable_up_down == "2":
            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, x**2)

            print()
            print("Scheitelpunkt: (0|0)")

            plt.plot(area, [((-2)**2), ((-1)**2), (0**2), (1**2), (2**2)])
            plt.show()

        elif opentop_opendownwards == "1" and stretched_compressed_or_not == "1" and move_parable_up_down == "2":
            stretched_compressed = float(input("Gestreckt oder gestaucht um: "))

            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, (stretched_compressed * x**2))

            print()
            print("Scheitelpunkt: (0|0)")

            plt.plot(area, [(stretched_compressed * (-2)**2), (stretched_compressed * (-1)**2), (stretched_compressed * 0**2),
                    (stretched_compressed * 1**2), (stretched_compressed * 2**2)])
            plt.show()

        elif opentop_opendownwards == "1" and stretched_compressed_or_not == "2" and move_parable_up_down == "1":
            move_parable = float(input("Verschoben um: "))

            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, (x**2 + move_parable))

            print()
            print("Scheitelpunkt: (0|" + str(move_parable) + ")")

            plt.plot(area, [((-2)**2 + move_parable), ((-1)**2 + move_parable), (0**2 + move_parable),
                    (1**2 + move_parable), (2**2 + move_parable)])
            plt.show()



        elif opentop_opendownwards == "2" and stretched_compressed_or_not == "1" and move_parable_up_down == "1":
            stretched_compressed = float(input("Gestreckt oder gestaucht um: "))
            move_parable = float(input("Verschoben um: "))

            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, (-stretched_compressed * x**2 + move_parable))

            print()
            print("Scheitelpunkt: (0|" + str(move_parable) + ")")

            plt.plot(area, [(-stretched_compressed * (-2)**2 + move_parable), (-stretched_compressed * (-1)**2 + move_parable),
                    (-stretched_compressed * 0**2 + move_parable), (-stretched_compressed * 1**2 + move_parable), (-stretched_compressed * 2**2 + move_parable)])
            plt.show()

        elif opentop_opendownwards == "2" and stretched_compressed_or_not == "2" and move_parable_up_down == "2":
            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, -x**2)

            print()
            print("Scheitelpunkt: (0|0)")

            plt.plot(area, [(-(-2)**2), (-(-1)**2), (-0**2), (-1**2), (-2**2)])
            plt.show()

        elif opentop_opendownwards == "2" and stretched_compressed_or_not == "2" and move_parable_up_down == "1":
            move_parable = float(input("Verschoben um: "))

            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, (-x**2 + move_parable))

            print()
            print("Scheitelpunkt: (0|" + str(move_parable) + ")")

            plt.plot(area, [(-(-2)**2 + move_parable), (-(-1)**2 + move_parable), (-0**2 + move_parable),
                    (-1**2 + move_parable), (-2**2 + move_parable)])
            plt.show()

        elif opentop_opendownwards == "2" and stretched_compressed_or_not == "1" and move_parable_up_down == "2":
            stretched_compressed = float(input("Gestreckt oder gestaucht um: "))

            print("---------------------------------------------------------------")
            for x in [-2, -1, 0, 1, 2]:
                print(x, (-stretched_compressed * x**2))

            print()
            print("Scheitelpunkt: (0|0)")

            plt.plot(area, [(-stretched_compressed * (-2)**2), (-stretched_compressed * (-1)**2), (-stretched_compressed * 0**2),
                    (-stretched_compressed * 1**2), (-stretched_compressed * 2**2)])
            plt.show()

elif only_yaxis == "j":
    apex_x = float(input("Scheitelpunkt für x: "))
    interval_1 = float(input("interval1: "))
    interval_2 = float(input("interval2: "))
    interval_3 = float(input("interval3: "))
    interval_4 = float(input("interval4: "))
    interval_5 = float(input("interval5: "))
    interval = [interval_1, interval_2, interval_3, interval_4, interval_5]
    print()
    opentop_opendownwards = input("Nach oben(1) oder unten(2) geöffnet? (1/2): ")
    stretched_compressed_or_not = input("gestreckt oder gestaucht(1) oder normal(2)? (1/2): ")
    move_parable_up_down = input("Nach oben oder unten(1) oder garnicht verschoben(2) (1/2): ")

    if opentop_opendownwards == "1" and stretched_compressed_or_not == "1" and move_parable_up_down == "1":
        stretched_compressed = float(input("Gestreckt oder gestaucht um: "))
        move_parable = float(input("Verschoben um: "))

        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, (stretched_compressed * (x + apex_x)**2 + move_parable))

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|" + str(move_parable) + ")")
        # print()
        # if opentop_opendownwards == "1" and move_parable > 0 or opentop_opendownwards == "2" and move_parable < 0:
        #     print("Nullstelle1 (N1): keine Nullstelle vorhanden")
        #     print("Nullstelle2 (N2): keine Nullstelle vorhanden")
        # else:
        #     try:
        #         p = (stretched_compressed * apex_x) + (stretched_compressed * apex_x) # funktioniert nur mit Formeln ohne stretched_compressed
        #         q = (stretched_compressed * apex_x) + move_parable                    # und apex_x = +1

        #         n1 = -(p / 2) + math.sqrt((p / 2)**2 - q)
        #         n2 = -(p / 2) - math.sqrt((p / 2)**2 - q)
        #         print("Nullstelle1 (N1): (" + str(n1) + "|0)")
        #         print("Nullstelle2 (N2): (" + str(n2) + "|0)")
        #     except:
        #         print("Nullstelle1 (N1): keine Nullstelle vorhanden")
        #         print("Nullstelle2 (N2): keine Nullstelle vorhanden")
        plt.plot(interval, [(stretched_compressed * (interval_1 + apex_x)**2 + move_parable),
                (stretched_compressed * (interval_2 + apex_x)**2 + move_parable), (stretched_compressed * (interval_3 + apex_x)**2 + move_parable),
                (stretched_compressed * (interval_4 + apex_x)**2 + move_parable), (stretched_compressed * (interval_5 + apex_x)**2 + move_parable)])
        plt.show()

    elif opentop_opendownwards == "1" and stretched_compressed_or_not == "2" and move_parable_up_down == "2":
        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, (x + apex_x)**2)

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|0)")

        plt.plot(interval, [(interval_1 + apex_x)**2, (interval_2 + apex_x)**2, (interval_3 + apex_x)**2, (interval_4 + apex_x)**2,
                (interval_5 + apex_x)**2])
        plt.show()

    elif opentop_opendownwards == "1" and stretched_compressed_or_not == "1" and move_parable_up_down == "2":
        stretched_compressed = float(input("Gestreckt oder gestaucht um: "))

        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, (stretched_compressed * (x + apex_x)**2))

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|0)")

        plt.plot(interval, [(stretched_compressed * (interval_1 + apex_x)**2), (stretched_compressed * (interval_2 + apex_x)**2),
                (stretched_compressed * (interval_3 + apex_x)**2), (stretched_compressed * (interval_4 + apex_x)**2),
                (stretched_compressed * (interval_5 + apex_x)**2)])
        plt.show()

    elif opentop_opendownwards == "1" and stretched_compressed_or_not == "2" and move_parable_up_down == "1":
        move_parable = float(input("Verschoben um: "))

        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, ((x + apex_x)**2 + move_parable))

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|" + str(move_parable) + ")")

        plt.plot(interval, [((interval_1 + apex_x)**2 + move_parable), ((interval_2 + apex_x)**2 + move_parable),
                ((interval_3 + apex_x)**2 + move_parable), ((interval_4 + apex_x)**2 + move_parable), ((interval_5 + apex_x)**2 + move_parable)])
        plt.show()


    
    elif opentop_opendownwards == "2" and stretched_compressed_or_not == "1" and move_parable_up_down == "1":
        stretched_compressed = float(input("Gestreckt oder gestaucht um: "))
        move_parable = float(input("Verschoben um: "))

        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, (-stretched_compressed * (x + apex_x)**2 + move_parable))

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|" + str(move_parable) + ")")

        plt.plot(interval, [(-stretched_compressed * (interval_1 + apex_x)**2 + move_parable),
                (-stretched_compressed * (interval_2 + apex_x)**2 + move_parable), (-stretched_compressed * (interval_3 + apex_x)**2 + move_parable),
                (-stretched_compressed * (interval_4 + apex_x)**2 + move_parable), (-stretched_compressed * (interval_5 + apex_x)**2 + move_parable)])
        plt.show()

    elif opentop_opendownwards == "2" and stretched_compressed_or_not == "2" and move_parable_up_down == "2":
        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, -(x + apex_x)**2)

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|0)")

        plt.plot(interval, [-(interval_1 + apex_x)**2, -(interval_2 + apex_x)**2, -(interval_3 + apex_x)**2,
                -(interval_4 + apex_x)**2, -(interval_5 + apex_x)**2])
        plt.show()

    elif opentop_opendownwards == "2" and stretched_compressed_or_not == "1" and move_parable_up_down == "2":
        stretched_compressed = float(input("Gestreckt oder gestaucht um: "))

        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, (-stretched_compressed * (x + apex_x)**2))

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|0")

        plt.plot(interval, [(-stretched_compressed * (interval_1 + apex_x)**2), (-stretched_compressed * (interval_2 + apex_x)**2),
                (-stretched_compressed * (interval_3 + apex_x)**2), (-stretched_compressed * (interval_4 + apex_x)**2),
                (-stretched_compressed * (interval_5 + apex_x)**2)])
        plt.show()

    elif opentop_opendownwards == "2" and stretched_compressed_or_not == "2" and move_parable_up_down == "1":
        move_parable = float(input("Verschoben um: "))

        print("---------------------------------------------------------------")
        for x in [interval_1, interval_2, interval_3, interval_4, interval_5]:
            print(x, (-(x + apex_x)**2 + move_parable))

        print()
        print("Scheitelpunkt: (" + str(interval_3) + "|" + str(move_parable) + ")")

        plt.plot(interval, [(-(interval_1 + apex_x)**2 + move_parable), (-(interval_2 + apex_x)**2 + move_parable),
                (-(interval_3 + apex_x)**2 + move_parable), (-(interval_4 + apex_x)**2 + move_parable), (-(interval_5 + apex_x)**2 + move_parable)])
        plt.show()
