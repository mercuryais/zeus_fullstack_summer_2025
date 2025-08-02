# X 1
def add_numbers(a, b):
    return a + b 
results = add_numbers(5, 3)
print(results)

# X 2
def get_user_info():
    name = "Alice"
    age = 30
    return name, age
print(get_user_info())
user_name ,user_age = get_user_info()

# X 3.1
def greet(name):
    return print("Hello, ", name, "!")

results = greet("Batsuuri")

# X 3.2
def multiply(a, b):
    results = a * b
    return results

print(multiply(2,5))

# X 3.3
def concatenate_strings(astr, bstr):
    fstr = astr + bstr
    return fstr

print(concatenate_strings("hello", " human"))

# X 3.4
def is_even(a):
    isEven = a % 2 == 0
    return isEven

print(is_even(201))

# X 3.5
def get_max(a, b):
    return max(a, b)

print(get_max(200, 100))

# X 3.6
def calculate_area_rectangle(w, h):
    aRec = w * h
    return aRec

print(calculate_area_rectangle(20, 30))

# X 3.7
def get_first_element(elements = []):
    if elements:
        return elements[0]    
    return None

print(get_first_element([10, 3, 5, 100, 200]))

# X 3.8
def power(a, b):
    return a**b

print(power(10, 3))

# Sequential search
# X 3.9
def find_max_in_list(my_list):
    for num in my_list:
        if num > max_value:
            max_value = num


print(find_max_in_list([2, 30 ,4]))

# X 3.10
def calculate_average(numbers):
    if not numbers:
        return None
    sum(numbers) / len(numbers)
print(calculate_average([200, 20, 10]))



