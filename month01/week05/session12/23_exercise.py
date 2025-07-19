import turtle 
import random  


turtle.colormode(255)
turtle.speed(0)
turtle.width(40)
for x in range(0, 180):
        turtle.color(x, 0, 0)
        turtle.goto(0, 0)
        turtle.right(2)
        turtle.fd(300)

turtle.done()