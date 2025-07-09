import random
import turtle

for n in range(10):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    turtle.goto(x, y)
    turtle.dot(20)

colours = ["Yellow", "Green", "Blue", "Grey", "rose"]
turtle.color(random.choice(colours))
radius = random.randint(1, 1000)
turtle.dot(radius)
turtle.done()