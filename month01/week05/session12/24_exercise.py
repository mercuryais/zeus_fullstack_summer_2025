import turtle 
import random  

turtle.colormode(255)
turtle.speed(0)
turtle.width(3)
for x in range(80, 200):
    turtle.color(0, x, 0)
    turtle.goto(0, 0)
    turtle.left(1)
    turtle.goto(0, 0)
    turtle.left(1)
    turtle.goto(0, 0)
    turtle.left(1)
    turtle.fd(500)

turtle.colormode(255)
turtle.speed(0)
turtle.width(40)
for x in range(0, 180):
        turtle.fd(250)
        turtle.color(x, 0, 0)
        turtle.goto(0, 0)
        turtle.right(1)
        turtle.goto(0, 0)
        turtle.right(1)
        turtle.fd(250)

turtle.width(6)
for x in range(81, 200):
        turtle.color(0, 0, x)
        turtle.fd(100)
        turtle.goto(0, 0)
        turtle.left(1)
        turtle.goto(0, 0)
        turtle.left(1)
        turtle.goto(0, 0)
        turtle.left(1)
        

turtle.done()