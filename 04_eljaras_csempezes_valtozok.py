import turtle

def helyre(teki, o, egys):
    '''Ez az eljárás középről a kiindulási helyére teszi a teknőcöt.
    A tolatás nagysága függ a csempék oldalhosszától
    és az egy sorban levő csempék számától. Tehát (o * egys).'''
    teki.back(o * egys)

def cs(teki, o):
    '''Ez az eljárás egyetlen, o oldalhosszú csempét rajzoltat a teknőccel.'''
    for j in range(4):
        teki.forward(o)
        teki.left(90)
    teki.forward(o)

def sor(teki, o, egys):
    '''Ez az eljárás egy sornyi csempét rajzoltat a teknőccel.
    Vegyük figyelemebe, hogy a teknőc már ismeri a cs() eljárást.'''
    for s in range(egys):
        cs(teki, o)
    teki.speed(1)
    teki.back(o * egys)
    teki.left(90)
    teki.forward(o)
    teki.right(90)
    teki.speed(0)

def fal(teki, o, egys, tobbs):
    '''Ez az eljárás egymás felett több sornyi csempét rajzoltat a teknőccel.
    Vegyük figyelemebe, hogy a teknőc már ismeri a
    cs(teki) eljárást, valamint a sor() eljárást.''' 
    for f in range(tobbs):
        sor(teki, o, egys)

#oldal = int(input("Mekkora legyen a csempe?  "))
#egysorban = int(input("Mennyi csempe legyen egy sorban?  "))
#sorok = int(input("Mennyi sor legyen egymás felett?  "))

ablak = turtle.Screen()
Eszti = turtle.Turtle()

Eszti.shape("turtle")
Eszti.color("blue")
Eszti.speed(1000)
Eszti.pensize(1)


helyre(Eszti, 20, 15)
#cs(Eszti, 20)
#sor(Eszti, 20, 15)
fal(Eszti, 20, 15, 5)

Eszti.shape("blank")
ablak.exitonclick()
