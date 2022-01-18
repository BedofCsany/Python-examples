def meddig_szamol(o):
    '''Meddig kell szamolni, hogy az osszeg a bekért összeg legyen a számok összege.'''
    '''Függvényt készítünk, ha csak egy visszaadott értéket várunk.'''
    szam = 1
    osszeg = 0
    while osszeg <= o:
        print(szam - 1, "\t", osszeg)
        osszeg = osszeg + szam
        szam = szam + 1
    return szam - 1



ossz = int(input("Mekkora összegig számoljunk? "))
ez_a_szam = meddig_szamol(ossz)
print("Ahhoz, hogy a számok összege nagyobb legyen mint", ossz, "eddig kell számolni:", ez_a_szam)

