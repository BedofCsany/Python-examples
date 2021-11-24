import random


def sorsol():
    dobas = random.randint(1, 2)
    if dobas == 1:
        penzoldal = "fej"
    else:
        penzoldal = "írás"
    return penzoldal


def diszito(n, sz):
    print()
    for i in range(n):
        print(sz, sep="", end="")
    print("\n")


tipp = input("Kérek egy tippet, fej lesz, avagy írás!    ")
eredmeny = sorsol()
print("Te ezt tippelted: ", tipp)
print("Én ezt dobtam: ", eredmeny)

if eredmeny == tipp:
    print("Nyertél, ügyes vagy!")
    diszito(100, "*")
else:
    print("Nem nyertél. Talán majd később!")
    diszito(100, "-")


