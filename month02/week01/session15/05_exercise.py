import turtle

def drawSpiral(side):
    turtle.width(20)
    turtle.fd(side)
    turtle.rt(45)
    if side > 10:
        drawSpiral(side - 5)
turtle.color('blue')
turtle.width(5)

# Function call
drawSpiral(120)
turtle.done()