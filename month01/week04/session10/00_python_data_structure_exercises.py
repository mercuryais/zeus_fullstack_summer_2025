# Variables

# X 1.1
message = "Hello World!"

# X 1.2
a, b = 7, 3

# X 1.3
firstname = "Batsuuri "
surname = 'Ayurzana'
fullname = firstname + surname

# X 1.4
x = 5
y = 10
temp = x
x = y
y = temp
del temp
print(x, y)

# X 1.5
var1 = '123'
num = int(var1)
print(num)

# 2.1
student = {
    'Name' : 'John',
    'Age' : 20,
    'Major' : "Physics"
    }

# 2.2
fruit_prices = {
    'apple': 1.5,
    'banana': 0.75
    }
fruit_prices['apple'] = 2.0
print(fruit_prices)

# 2.3
fruit_prices['orange'] = 1.25
del fruit_prices['banana']
print(fruit_prices)

# 2.4
print(student.keys())
print(student.values())

# 2.5
student_grades = {
    'Batsuuri' : {
        'Math' : 45,
        'Science' : 67
    },
    'Orgil' : {
        'Math' : 23,
        'Science' : 54
    }
}
print(student_grades)

# 3.1
colors = ['red', 'green', 'blue']

# 3.2
colors.append("yellow")
colors[1] = "orange"
print(colors)

# 3.3
print(colors[0])
print(colors[-1])
print(colors[0:3])

# 3.4
print(colors.index("blue"))
del colors[1]

# 3.5
# ??
 
# 4.1
dimensions = 200, 50
print(dimensions[1])

# 4.2
point = (3, 4)
x, y = point
print(y)

# 4.3
# dimensions[0] = 12

# 4.4
coordinates = ((1,2), (3,4), (5,6))
print(coordinates)

# 4.5
wd = {
    (0,0) : 'origin',
    (0,1) : 'pointA',
    (4,2) : 'pointB',
    (4,6) : 'pointC'
}

# 5.1
greetings = "Hello "
name = 'Alice'
message = greetings + name
print(message)

# 5.2
word = 'Programming'
print(word[0])
print(word[-1])
print(word[3:7])

# 5.3
text = ' Python is fun! '
changed1 = text.replace(" ", "")
changed2 = changed1.upper()
changed3 = changed2.replace("FUN", "POWERFUL")
print(changed3)

# 5.4
name = "HEHA"
age = 123
print(f"My name is", name, "and I am", age, "years old.")

# 5.5
theText = "Hello, user!\nThis is the first line.\nAnd this is the second line."
print(theText)

again = '''Hello, user!
This is the first line.
And this is the second line.'''
print(again)
