def hetnapja(sorszam):
    if sorszam < 1:
        print('Ilyen sorszámú nap nincsen!')
    elif sorszam == 1:
        print('hétfő')
    elif sorszam == 2:
        print('kedd')
    elif sorszam == 3:
        print('szerda')
    elif sorszam == 4:
        print('csütörtök')
    elif sorszam == 5:
        print('péntek')
    elif sorszam == 6:
        print('szombat')
    elif sorszam == 7:
        print('vasárnap')
    else:
        print('Ennyiedik nap nincsen!')


hanyadik = int(input('Hányadik nap van a héten?   '))

hetnapja(hanyadik)