# While we are talking about looping ...

# loop- davtlalt
for step in range(0, 20):
    print(step)

# while loop
step = 0
tired = False
bad_weather = False

while step < 10000:
    print(step)

    if tired == True:
        break

    elif bad_weather == True:
        break
    
    else:
        step = step + 1

print("out of the while loop!")

# Example 02
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)
