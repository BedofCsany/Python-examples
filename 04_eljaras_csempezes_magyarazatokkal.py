import turtle

def helyre(teki):
    '''Ez az eljárás középről a kiindulási helyére teszi a teknőcöt.
    A tolatás nagysága függ a csempék oldalhosszától
    és az egy sorban levő csempék számától. Tehát (oldal * egysorban).'''
    teki.back(oldal * egysorban)

def cs(teki):
    '''Ez az eljárás egyetlen, oldal oldalhosszú csempét rajzoltat a teknőccel.'''
    for j in range(4):
        teki.forward(oldal)
        teki.left(90)
    teki.forward(oldal)

def sor(teki):
    '''Ez az eljárás egy sornyi csempét rajzoltat a teknőccel.
    Vegyük figyelemebe, hogy a teknőc már ismeri a cs(teki) eljárást.'''
    for s in range(egysorban):
        cs(teki)
    teki.speed(1)
    teki.back(oldal * egysorban)
    teki.left(90)
    teki.forward(oldal)
    teki.right(90)
    teki.speed(0)

def fal(teki):
    '''Ez az eljárás egymás felett több sornyi csempét rajzoltat a teknőccel.
    Vegyük figyelemebe, hogy a teknőc már ismeri a
    cs(teki) eljárást, valamint a sor(teki) eljárást.''' 
    for f in range(sorok):
        sor(teki)

oldal = int(input("Mekkora legyen a csempe?  "))
egysorban = int(input("Mennyi csempe legyen egy sorban?  "))
sorok = int(input("Mennyi sor legyen egymás felett?  "))

ablak = turtle.Screen()
Eszti = turtle.Turtle()

Eszti.shape("turtle")
Eszti.color("blue")
Eszti.speed(1000)
Eszti.pensize(1)


helyre(Eszti)
#cs(Eszti)
#sor(Eszti)
fal(Eszti)

Eszti.shape("blank")
ablak.exitonclick()
