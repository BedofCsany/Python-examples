def szamjegy_szam(n):
    n = abs(n)
    szamlalo = 0
    while n != 0:
        szamlalo = szamlalo + 1
        m = n % 10
        n = n // 10
        print(n, "\t", m)
    return szamlalo

szam = int(input('Kérek egy számot! '))
print(szamjegy_szam(szam))