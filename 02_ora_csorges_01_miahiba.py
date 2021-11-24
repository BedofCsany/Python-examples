ora = int(input("Hány óra van? "))
ora_mulva = int(input("Hány óra múlva csörögjek? "))

nap_mulva = ora_mulva // 24
maradek_ora = ora_mulva % 24
csengetes_ora = ora + maradek_ora

print(nap_mulva, "nap múlik el.")
print(maradek_ora, "óra marad.")
print(csengetes_ora, "órakor fog csörögni.")

# Próbáld ki!
# Ad-e rossz megoldást a program?
# Milyen hiba ez?
# Hogyan lehet javítani?
