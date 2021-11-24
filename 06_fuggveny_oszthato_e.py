def oszthato_e(x, y):
    """ Annak vizsgálata, hogy x osztható-e y-nal. """
    if x % y == 0:
        valasz = "Osztható!"
        return valasz
    else:
        valasz = "Nem osztható!"
        return valasz
    
osztando = int(input("Kérek egy osztandót!  "))
oszto = int(input("kérek egy osztót!  "))

eredmeny = oszthato_e(osztando, oszto)
print(eredmeny)
