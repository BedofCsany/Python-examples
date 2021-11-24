import turtle

ablak = turtle.Screen()       # Hozd létre az ablak objektumot!
ablak.bgcolor("lightgreen")   # Állítsd be az ablak objektum tulajdonságait!
ablak.title("Eszti & Sanyi")

Eszti = turtle.Turtle()       # Hozd létre Eszti objektumot!
Eszti.color("hotpink")        # Állítsd be Eszti objektum tulajdonságait!
Eszti.pensize(2)

Sanyi = turtle.Turtle()       # Hozd létre Sanyi objektumot!

Eszti.forward(80)             # Rajzoltass Esztivel egy egyenlő oldalú háromszöget!
Eszti.left(120)
Eszti.forward(80)
Eszti.left(120)
Eszti.forward(80)
Eszti.left(120)               # Fejezd be a háromszöget!

Eszti.right(180)              # Eszti forduljon meg!
Eszti.forward(80)             # Mozdítsd el őt a kiindulóponttól!

# Rajzoltass Sanyival egy négyzetet!
for i in [0, 1, 2, 3]:
    Sanyi.forward(60)
    Sanyi.left(90)
    

ablak.exitonclick()
