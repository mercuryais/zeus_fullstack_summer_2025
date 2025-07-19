import turtle

turtle.speed(0)
turtle.colormode(255)

#RGB (red, green, blue) - channel

for x in range(0, 200):
    turtle.color(x, 255, x)
    turtle.goto(x, 0)
    turtle.goto(x, 200)

turtle.done()