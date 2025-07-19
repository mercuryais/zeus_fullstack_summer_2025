import turtle 

turtle.colormode(255)
turtle.speed(0)
turtle.goto(-200, -200)

for x in range(0, 500):
    turtle.color(0, 0, 0)
    turtle.goto(x, -200)
    turtle.goto(x, 300)

turtle.width(100)
turtle.goto(100,100)
for sphere in range(255, 0, -1):
    turtle.color(255, sphere, 0)
    turtle.dot(sphere)
    
    
turtle.done() 