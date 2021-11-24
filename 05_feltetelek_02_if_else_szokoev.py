evszam = int(input("Kérek egy évszámot, 1900 és 2021 között: "))
if evszam % 4 == 0:
    print("Ez az év szökőév volt.")
else:
    print("Ez az év nem szökőév volt.")
