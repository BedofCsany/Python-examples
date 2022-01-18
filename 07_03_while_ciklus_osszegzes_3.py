szam = 1
osszeg = 0
while osszeg <= 1000000:
    print(szam - 1, "\t", osszeg)
    osszeg = osszeg + szam
    szam = szam + 1
print(szam -1, "\t", osszeg)