osszes_masodperc = int(input("Összesen hány másodperc? "))

osszes_ora = osszes_masodperc // 3600
maradek_masodperc = osszes_masodperc % 3600

print("Ez: ", osszes_ora, " óra.")
print("Maradt még: ", maradek_masodperc, "másodperc.")

maradek_perc = maradek_masodperc // 60
maradek_masodperc = maradek_masodperc % 60

print("Ez: ", maradek_perc, " perc,")
print("Maradt a végén: ", maradek_masodperc, " másodperc.")


