def oszto_szam(n):
    feleig = n // 2 + 1
    for oszto_e in range(2, feleig):
        if n % oszto_e == 0:
            oszto = oszto_e
            print(oszto, end=", ")
szam = int(input('Kérek egy számot! '))
oszto_szam(szam)

