a = int(input("Kérek egy számot!  a=  "))
b = int(input("Kérek egy számot!  b=  "))
c = int(input("Kérek egy számot!  c=  "))

ln = 0
if a == b:
    ln = a = b
    lnst = "Az a == b-vel "
    if ln == c:
        ln = a = b = c
        print("Mindhárom szám ugyanannyi volt.")
    elif ln > c:
        print(lnst, "és ők a legnagyobbak.")
    else:
        ln = c
        lnst = "A c szám "
        print(lnst, "a legnagyobb: ", ln)

if a > b:
    ln = a
    lnst = "Az a szám "
    if ln == c:
        print("A c == a-val, és ők a legnagyobbak.")
    elif ln < c:
        ln = c
        lnst = "A c szám "
        print(lnst, "a legnagyobb: ", ln)
    else:
        print(lnst, "a legnagyobb: ", ln)

if b > a:
    ln = b
    lnst = "A b szám "
    if ln == c:
        print("A c == b-vel, és ők a legnagyobbak.")
    elif ln < c:
        ln = c
        lnst = "A c szám "
        print(lnst, "a legnagyobb: ", ln)
    else:
        print(lnst, "a legnagyobb: ", ln)