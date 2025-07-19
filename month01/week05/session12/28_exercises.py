import turtle 

turtle.colormode(255)
turtle.speed(0)

for x in range(0, 200):
    turtle.color(0, 0, 0)
    turtle.goto(x, 0)
    turtle.goto(x, 200)

turtle.width(100)
turtle.goto(0,0)
for sphere in range(255, 0, -1):
    turtle.color(255, sphere, 0)
    turtle.dot(sphere)
    
    
turtle.done() 