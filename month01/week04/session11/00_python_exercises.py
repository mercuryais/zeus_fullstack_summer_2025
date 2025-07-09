import turtle

turtle.speed(0)
turtle.width(3)

for s in range(10):
    turtle.right(36)
    for i in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
turtle.done()