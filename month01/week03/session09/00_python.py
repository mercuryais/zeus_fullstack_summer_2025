# Python Variables

# X 1
num = 7

# X 2
a = 5
b = 8
temp = a
a = b
b = temp
del temp
print(a, b)

# X 3
x = 15
y = 25
total = y + x

# X 4
my_name = "Batsuuri"
print(type(my_name))

# X 5
lenght = 10
width = 5
area = lenght * width

# X 6
score = 42
score = score + 42

# X 7
a, b ,c = 3, 6, 9
print(a, b, c)

# X 8 
isTheSkyBlue = True

# X 9
color = "Black"
print("My favorite color is: ", color)
print(f"My favorite color is: {color}")

# X 10
integer = 4 
flo = 3.7
result = integer + flo
print(result, type(result))

# Pythin List

# X 1
fruits = ["apple", "banana", "cherry"]
# why need square brackets for list

# X 2
print(fruits[0])
print(fruits[-1])

# X 3
fruits.append("orange")

# X 4
del fruits[1]

# X 5
print(len(fruits))

# X 6
numbers = [2, 5, 8, 12, -3, -5]
numbers.sort()
print(numbers)

# X 7
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])

# X 8
list = [1, 2, 3]
list2 = [4, 5, 6]
list.extend(list2)
print(list)
# Why square brackets are seen
# list2 becomes one element and added into list

# X 9
print("mango" in fruits)

# X 10
squares = [x**2 for x in range(1, 6)]
print (squares)
# how this works ^^

# Python Strings

# X 1
quote = "Hello who we dont do what should yes or no"

# X 2
print(len(quote))

# X 3
print(quote[-1])

# X 4
print(quote[0:5])

# X 5
a = "Hello "
b = "World"
greetings = a + b
print(greetings)

# X 6
print(quote.upper())

# X 7
print(quote.count("ll"))

# X 8
print(quote.replace("who", "ME"))

# X 9
color = "red, green, blue"
splitted = color.split()
print(splitted[0])

# X 10
print(quote.startswith("The"))
