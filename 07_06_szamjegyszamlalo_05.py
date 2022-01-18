def szamjegyszam_05(n):
    szamlalo = 0
    while n > 0:
        maradek = n % 10
        print(maradek)
        if maradek == 0 or maradek == 5:
            szamlalo += 1
        n = n // 10
    return szamlalo

print(szamjegyszam_05(1055030250))