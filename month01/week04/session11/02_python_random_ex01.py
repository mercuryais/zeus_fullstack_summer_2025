import turtle
import random

i = int(input("Heden zuraas awah ve"))
colours = ['blue', 'red', 'purple', 'pink', 'yellow', 'green']
for n in range(i):
    width = random.randint(1, 200)
    angle = random.randint(30, 330)
    turtle.color(random.choice(colours))
    turtle.forward(width)
    turtle.right(angle)
turtle.done()





