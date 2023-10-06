import turtle
 
screen = turtle.Screen()
screen.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("brown")
t.speed(1.5)
 
def dibujar_petal(t, radio):
    t.pensize(2)
    t.pencolor("black")
    t.color("yellow")
    t.begin_fill()
    t.circle(radio, 60)
    t.left(120)
    t.circle(radio, 60)
    t.end_fill()
    t.pencolor("brown")
    t.pensize(1)

def dibujar_girasol():
    radio = 50
 
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(4)
    t.left(90)
    t.color("")
    t.forward(100)
    
    for _ in range(18):
        dibujar_petal(t, radio)
        t.right(20)
    
    t.color("brown")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
 
# t.penup()
# t.goto(-400, -100)
# t.pendown()
# t.color("green")
# t.begin_fill()
# for _ in range(2):
#     t.forward(800)
#     t.right(90)
#     t.forward(200)
#     t.right(90)
# t.end_fill()
 
for _ in range(4):
    dibujar_girasol()

t.penup()
t.goto(0, 180)
t.color("red")
t.write("¡Eres la cosita más preciosa mi Donita!", align="center", font=("Arial", 12, "bold"))

t.goto(0, -200)
t.color("red")
t.write("¡Te amo muchisimo!", align="center", font=("Arial", 12, "bold"))
t.pendown()


t.hideturtle()
turtle.done()