import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.shape("turtle")
Eszti.color("blue")

Eszti.penup()                # Ez új
meret = 100
for i in range(12):
    Eszti.forward(meret)
    Eszti.pendown()
    Eszti.forward(meret/4)
    Eszti.penup()
    Eszti.forward(meret/5)
    Eszti.stamp()             # Hagyj egy lenyomatot a vásznon!
    Eszti.back(meret+meret/4+meret/5)      # Mozgasd ...
    Eszti.right(30)           #  ...  és fordítsd Esztit!

ablak.mainloop()
