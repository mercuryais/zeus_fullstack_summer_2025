import turtle 

turtle.colormode(255)
turtle.speed(0)
for n in range(0, 200):
    turtle.color(n, 0, 0)
    turtle.dot(250-n)

turtle.done()