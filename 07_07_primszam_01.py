import math

def prim_szam(n):
    negyzetgyok = math.sqrt(n)
    prim = True
    for oszto in range(2, int(negyzetgyok) + 1):
        print(oszto)
        if n % oszto == 0:
            prim = False
            break
        else:
            prim = True
    if prim:
        valasz = "Prímszám."
        return valasz
    else:
        valasz = "Nem prímszám."
        return valasz
        
szam = int(input('Kérek egy számot! '))
akkor_mi_is = prim_szam(szam)
print(akkor_mi_is)

