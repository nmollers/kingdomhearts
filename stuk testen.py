def snow_world_1():
    keuze1 = input("Go to the Toy Factory?> ")
    while True:
        if keuze1 == 'yes':
            print("verhaal gaat hier verder")
        elif keuze1 == 'no':
            print("There is no other choise then go to the factery")
        else:
            print("Please enter a valid input")
            break

snow_world_1()