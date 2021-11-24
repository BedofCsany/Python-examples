def ketbetus_szo_keresese(szolista):
    for szo in szolista:
        if len(szo) == 2:
            return szo
    return ""

def mondat_keszites(szolista):
    mondat = ""
    for szo in szolista:
        mondat = mondat + szo
        mondat = mondat + " "
    return mondat
        
        
#A 'ketbetus_szo_keresese()' függvény tesztelése
egyik_mondat = mondat_keszites(["Ez",  "egy", "sárga", "papagáj."])
print(egyik_mondat)
print(ketbetus_szo_keresese(["Ez",  "egy", "sárga", "papagáj."]))

masik_mondat = mondat_keszites(["Szeretem",  "a",  "sajtot", "!!"])
print(masik_mondat)
print(ketbetus_szo_keresese(["Szeretem",  "a",  "sajtot", "!!"]))

harmadik_mondat = mondat_keszites(["Kerüld", "a", "print", "és", "az", "input", "függvényeket", "a", "produktív", "függvényeken", "belül!!"])
print(harmadik_mondat)
print(ketbetus_szo_keresese(["Kerüld", "a", "print", "és", "az", "input", "függvényeket", "a", "produktív", "függvényeken", "belül!!"]))