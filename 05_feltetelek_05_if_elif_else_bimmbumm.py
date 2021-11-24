for szam in range(1, 201):
    if szam % 3 == 0 and szam % 5 == 0:
        print("BimmBumm")
    elif szam % 3 == 0:
        print("Bimm")
    elif szam % 5 == 0:
        print("Bumm")
    else:
        print(szam)