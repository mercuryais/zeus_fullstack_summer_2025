import turtle
import random

i = int(input("Heden zuraas awah ve"))
colours = ['blue', 'red', 'purple', 'pink', 'yellow', 'green']
turtle.bgcolor("CadetBlue2")
turtle.width(8)
turtle.speed(0)
for n in range(i):
    width = random.randint(170, 250)
    angle = random.randint(30, 330)
    turtle.right(angle)
    turtle.color(random.choice(colours))
    turtle.forward(width)
    turtle.right(180)
    turtle.forward(width)
turtle.done()