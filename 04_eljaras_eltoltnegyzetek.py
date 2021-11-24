import turtle

    
def rajzhoz(teki):
    teki.penup()
    teki.bk(200)
    teki.pendown()       

def negyzet(teki, oldal):
    for osz in range(4):
        teki.fd(oldal)
        teki.lt(90)
        
def kihagyas(teki, kih):
    teki.penup()
    teki.fd(kih)
    teki.pendown()


    
ablak = turtle.Screen()    
ablak.bgcolor("lightgreen")
ablak.title("Eltolt négyzetek")    

Sanyi = turtle.Turtle()
Sanyi.pencolor("red")
Sanyi.pensize(2)


rajzhoz(Sanyi)

for db in range(5):
    negyzet(Sanyi, 50)
    Sanyi.fd(50)
    kihagyas(Sanyi, 60)

ablak.exitonclick()