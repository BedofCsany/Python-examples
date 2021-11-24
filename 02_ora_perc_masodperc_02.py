# Másodpercek átszámítása órákká, percekké, másodpercekké.

osszes_masodperc = int(input("Összesen hány másodperc? "))
''' A másodpercek darabszáma egész szám, így az input() függvényben
a felhasználótól kapott sztring értéket rögtön átalakítjuk egész számmá
az int() függvénnyel.'''


osszes_ora = osszes_masodperc // 3600
maradek_masodperc = osszes_masodperc % 3600

print("Ez: ", osszes_ora, " óra, mert az", osszes_ora, "* 3600 másodperc, az ", osszes_ora * 3600, "másodperc."  )
print("Maradt még: ", maradek_masodperc, "másodperc.")

maradek_perc = maradek_masodperc // 60
maradek_masodperc = maradek_masodperc % 60

print("Ez: ", maradek_perc, " perc, mert az", maradek_perc, "* 60 perc, az ", maradek_perc * 60, "másodperc."  )
print("Maradt a végén: ", maradek_masodperc, " másodperc.")

print("Tehát: ", osszes_masodperc, "másodperc, az annyi mint", osszes_ora, "óra,", maradek_perc, "perc,", maradek_masodperc, "másodperc.")
