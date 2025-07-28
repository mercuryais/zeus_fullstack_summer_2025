import turtle
turtle.width(20)
def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(25)
    if side > 10:
        drawSpiral(side - 2)
turtle.color('purple')
turtle.width(10)

# Function call
drawSpiral(120)
turtle.done()