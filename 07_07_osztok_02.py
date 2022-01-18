def oszto_szam(n):
    feleig = n // 2 + 1
    osztok_szama = 0
    for oszto_e in range(2, feleig):
#        print(oszto_e)
        if n % oszto_e == 0:
            oszto = oszto_e
            print(oszto, end=", ")
            osztok_szama +=1
    return osztok_szama
szam = int(input('Kérek egy számot! '))
print("Osztók száma:", oszto_szam(szam))

