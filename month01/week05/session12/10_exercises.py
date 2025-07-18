import turtle 
import random  

col = ['yellow', 'red', 'orange']
turtle.colormode(255)
turtle.speed(0)
turtle.width(5)

for a in range(0, 360):
    turtle.color(random.choice(col))
    turtle.goto(0, 0)
    turtle.left(1)
    turtle.fd(700)

turtle.done()