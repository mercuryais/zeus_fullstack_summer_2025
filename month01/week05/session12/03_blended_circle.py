import turtle

turtle.colormode(255)
turtle.speed(0)
turtle.width(3)

for a in range(0, 180):
    turtle.goto(0, 0)
    turtle.color(255, a, 0)
    turtle.right(2)
    turtle.fd(300)

turtle.done()