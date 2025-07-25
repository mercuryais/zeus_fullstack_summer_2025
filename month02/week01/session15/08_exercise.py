import turtle

def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(90)
    if side > 10:
        drawSpiral(side - 5)
turtle.color('green')
turtle.width(5)

# Function call
drawSpiral(170)
turtle.done()