def ketbetus_szo_keresese(szolista):
    for szo in szolista:
        if len(szo) == 2:
            return szo
    return ""


#A 'ketbetus_szo_keresese()' függvény tesztelése
print(ketbetus_szo_keresese(["Ez",  "egy", "sárga", "papagáj", "."]))
print(ketbetus_szo_keresese(["Szeretem",  "a",  "sajtot", "!!"]))
print(ketbetus_szo_keresese(["Nem", "tudom", "hogy", "van-e", "itt", "kétbetűs", "szó", "?"]))