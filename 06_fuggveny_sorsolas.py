import random


def sorsol():
    dobas = random.randint(1, 2)
    if dobas == 1:
        penz = "fej"
    else:
        penz = "írás"
    return penz


for s in range(10):
    eredmeny = sorsol()
    print("Én ezt dobtam: ", eredmeny )

