def ter(r):
    t = 3.14159 * r ** 2
    return t




sugar = float(input("Mekkora a kör sugara?   "))

nyers_terulet = ter(sugar)

print(nyers_terulet)

kor_terulet = round(nyers_terulet, 3)

print ("A kör területe:  ", kor_terulet)