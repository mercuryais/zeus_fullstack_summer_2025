import random
import turtle

paint = ['red', 'blue', 'pink']
turtle.color(random.choice(paint))
a = random.randint(80, 800)
turtle.dot(a)
turtle.done()