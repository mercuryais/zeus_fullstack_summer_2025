import turtle 
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)
for n in range(0, 200):
    turtle.color(255, 250-n, 0)
    turtle.dot(300-n)

turtle.done() 