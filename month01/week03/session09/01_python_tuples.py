# Python tuples
fibs = (0, 1, 1, 2, 3)
print(fibs)
# coordinate system
A = (100, 50)

# Example list
changed_list = [1, 2, 4, 5]
print(changed_list)
changed_list[1] = 3
print(changed_list)

# try to change tuples
# fibs[0] = 2

# get item of tuples
print(fibs[0])

fruits = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(fruits)


# type of tuple
print(type(fruits)) # <class 'tuple'>

# mixed tuples 
mixed_tuple = ("abc", 34, 35.6, "male")
print(mixed_tuple)

# make tuple
new_tuple = tuple(("cherry", "apple", "banana"))
print(new_tuple)

array_tuple = tuple([1, 3, 4, 5])
print(array_tuple)

# convert from tuple to list
number_tuple = (4, 5, 6, 7)
print(number_tuple)
number_list_from_tuple = list(number_tuple)
print(number_list_from_tuple)

# unpack tuples
packed_tuple = ('banana', 'apple')
fruit1, fruit2 = packed_tuple
print(fruit1)
print(fruit2)