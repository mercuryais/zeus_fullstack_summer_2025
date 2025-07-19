import turtle 
import random  

turtle.colormode(255)
turtle.speed(0)
turtle.width(2)
for x in range(20, 200):
        turtle.color(0, 0, x)
        turtle.goto(0, 0)
        turtle.left(1)
        turtle.fd(250)

turtle.done()