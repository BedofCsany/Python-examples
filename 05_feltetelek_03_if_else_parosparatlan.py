szam = int(input("Kérek egy számot!    "))

maradek = szam % 2

if maradek == 0:
    print("Ez egy páros szám.")
    print("Tudtad, hogy a 2 az egyetlen páros prímszám?")
else:
    print("Ez egy páratlan szám.")
    print("Tudtad, hogy két páratlan számot összeszorozva " + "az eredmény mindig páratlan?")