def oszthato_e(x, y):
    """ Annak vizsgálata, hogy x osztható-e y-nal. """
    return x % y == 0
    
osztando = int(input("Kérek egy osztandót!  "))
oszto = int(input("kérek egy osztót!  "))

if oszthato_e(osztando, oszto):
    print("Osztható!")
else:
    print("Nem osztható!")