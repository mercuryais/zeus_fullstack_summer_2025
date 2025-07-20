import turtle 
import random  

turtle.colormode(255)
turtle.speed(0)
turtle.width(2)
for x in range(20, 200):
        turtle.color(0, x, 0)
        
        turtle.left(2)
        turtle.fd(250)
        turtle.goto(0, 0)

turtle.width(40)
for x in range(0, 180):
        turtle.color(x, 0, 0)
        turtle.right(2)
        turtle.fd(150)
        turtle.goto(0, 0)

turtle.width(6)
for x in range(40, 220):
        turtle.color(0, 0, x)
        turtle.fd(100)
        turtle.goto(0, 0)
        turtle.left(2)
        
turtle.done()