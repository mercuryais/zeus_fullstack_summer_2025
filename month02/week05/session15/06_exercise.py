import turtle

def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(45)
    if side > 10:
        drawSpiral(side - 5)
turtle.color('red')
turtle.width(10)

# Function call
drawSpiral(130)
turtle.done()
