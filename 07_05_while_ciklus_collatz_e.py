def collatz(n):
    ''' Kiírja a Collatz sorozatot n-től amíg el nem éri az 1-et. '''
    ''' Eljárást készítünk, mert sok rész-eredményt kell kiírnunk.'''
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:        # Vizsgálat, hogy n páros szám-e.
            n = n // 2        # Ha n páros szám.
        else:                 
            n = n * 3 + 1     # Ha n páratlan szám.
    print(n, end=".\n")
    

kiindulo_szam = int(input("Mekkora legyen a kiinduló szám? "))
collatz(kiindulo_szam)