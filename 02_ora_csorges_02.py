# Adatbekérés.
ora = int(input("Hány óra van? "))
ora_mulva = int(input("Hány óra múlva csörögjek? "))

# Számítások.
nap_mulva = ora_mulva // 24
maradek_ora = ora_mulva % 24
csengetes_ora = ora + maradek_ora

# Egy kis korrekció, ha szükséges.
if csengetes_ora > 24:
    csengetes_ora = csengetes_ora - 24
    nap_mulva = nap_mulva + 1
    
# Eredménykiírás.
print(nap_mulva, "nap múlik el.")
print(maradek_ora, "óra marad.")
print(csengetes_ora, "órakor fog csörögni.")

