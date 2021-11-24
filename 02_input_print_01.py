# Bekérjük a felhasználótól a kör sugarának értékét.
bemenet = input("Mekkora a kör sugara? ")

# Ez egy karaktersor (sztring), lesz a bemenet változó értéke.
# Próbáld ki! Vedd ki a # jelet az alabbi sorbol és futtasd úgy a programot.
#print("A bemenet változó típusa: ", type(bemenet))
''' Alakítsuk át tizedestörtté, a 'bemenet' változót és
tegyük bele egy 'sugar' nevű változóba.'''
sugar = float(bemenet)

# Egy tizedestört (float), lesz a sugar változó értéke.
# Próbáld ki! Vedd ki a # jelet az alabbi sorbol és futtasd úgy a programot.
#print("A sugar változó típusa: ", type(sugar))
''' Kiszámítjuk a jobb oldali kifejezés értékét és
elhelyezzük egy 'terulet' nevű változóban.'''
terulet = 3.14159 * sugar ** 2

''' A print függvény kettő dolgot ír ki:
- egy "A terület:" tartalmú sztringet, és
- a 'terulet' változó értékét
a kettő közé egy szóköz kerül.'''
print("A terület: ", terulet)
input ("A befejezéshez, nyomja meg az ENTER-t!")


