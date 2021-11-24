def hetnapja(sorszam):
    if sorszam < 1:
        valasz = ('Ilyen sorszámú nap nincsen!')
        return valasz
    elif sorszam == 1:
        valasz = ('hétfő')
        print(valasz)
        return valasz
    elif sorszam == 2:
        valasz = ('kedd')
        return valasz
    elif sorszam == 3:
        valasz = ('szerda')
        return valasz
    elif sorszam == 4:
        valasz = ('csütörtök')
        return valasz
    elif sorszam == 5:
        valasz = ('péntek')
        return valasz
    elif sorszam == 6:
        valasz = ('szombat')
        return valasz
    elif sorszam == 7:
        valasz = ('vasárnap')
        return valasz
    else:
        valasz = ('Ennyiedik nap nincsen!')
        return valasz


hanyadik = int(input('Hányadik nap van a héten?   '))

melyiknap = hetnapja(hanyadik)
print(melyiknap)
print(valasz)


#print(hetnapja(hanyadik))