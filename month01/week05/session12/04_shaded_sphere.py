import turtle

turtle.colormode(255)
turtle.speed(0)

for size in range(255, 0, -1):
    turtle.color(255, 128, size)
    turtle.dot(2 * size)

turtle.done()