def greet():
    print("Сайн уу, Функц!")
greet()

# 2
def greet_by_name(name):
    print(f"Сайн уу, {name}!")
greet_by_name("Болд")
greet_by_name("Сарнай")

# 3
def add_and_print(a, b):
    print(a + b)
add_and_print(5, 3)
add_and_print(100, 200)

# 4
def add_and_return(a, b):
    return a + b
hariu = add_and_return(10, 20)
print(f"Функцээс буцаасан утга: {hariu}")
print(f"Шууд хэвлэх: {add_and_return(-5, 5)}")

# 5
def calculate_rectangle_area(length, width):
    return length * width
talbai1 = calculate_rectangle_area(10, 5)
print(f"10x5 хэмжээтэй тэгш өнцөгтийн талбай: {talbai1}")

# 6
def is_even(number):
    return True if number % 2 == 0 else False
print(f"10 тэгш тоо мөн үү? {is_even(10)}")
print(f"7 тэгш тоо мөн үү? {is_even(7)}")

# 7
def power(base, exponent):
    return base**exponent
print(f"2-ын 3 зэрэг: {power(2, 3)}")
print(f"5-ын 2 зэрэг: {power(5, 2)}")

# 8
def get_first_char(word):
    return word[0]
print(f"'Python' гэдэг үгний эхний үсэг: {get_first_char('Python')}")

# 9
def greet_country(name, country="Монгол"):
    print(f"Сайн уу, {name}! Та {country} улсаас мэндчилж байна.")
greet_country("Дорж") 
greet_country("John", "АНУ")

# 10
def find_max(a, b):
    return max(a, b)
print(f"100 ба 200-ийн их нь: {find_max(100, 200)}")

# 11
def find_max_of_three(a, b, c):
    max = find_max(a, b)
    max = find_max(max, c)
    return max
print(f"10, 25, 15-ын хамгийн их нь: {find_max_of_three(10, 25, 15)}")

# 12
def circle_stats(radius):
    pi = 3.14
    return pi * radius * 10, pi * 2 * radius
talbai, perimetr = circle_stats(10)
print(f"10 радиустай тойргийн талбай: {talbai}, периметр: {perimetr}")

# 13
def sum_list(numbers):
    max = 0
    for number in numbers:
        max = max + number
    return max
my_list = [1, 2, 3, 4, 5]
print(f"{my_list} жагсаалтын нийлбэр: {sum_list(my_list)}")

# 14
def count_vowels(sentence):
    vowels = "аэиоу"
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count
print(f"'Сайн байна уу' гэдэгт {count_vowels('Сайн байна уу')} эгшиг бий.")

# 15
def describe_pet(animal_type, pet_name):
    print(f"Надад {animal_type} байдаг.\nТүүний нэрийг {pet_name} гэдэг.")
describe_pet(pet_name="Банхар", animal_type="нохой")

# 16
def celsius_to_fahrenheit(celsius):
    return celsius *9/5 + 32
c = 25
f = celsius_to_fahrenheit(c)
print(f"{c}°C нь {f}°F-тэй тэнцүү.")

# 17
def fizzbuzz_check(number):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
for i in range(1, 21):
    (fizzbuzz_check(i))

# 18
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

# 19
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
print(f"5-ын факториал: {factorial_recursive(5)}")

# 20
def is_prime(num):
    isPrime = True
    for x in range(num):
        if x > 1:
            if num % x == 0:
                isPrime = False
    return isPrime
print(f"13 анхны тоо мөн үү? {is_prime(13)}")
print(f"12 анхны тоо мөн үү? {is_prime(12)}")

# 21 
square = lambda x: x**2
print(f"5-ын квадрат: {square(5)}")
print(f"10-ын квадрат: {square(10)}")

# 22
def reverse_list(items):
    reversed = []
    for item in items:
        reversed.insert(0, item)
    return reversed
original_list = [10, 20, 30, 40, 50]
reversed_list = reverse_list(original_list)
print(f"Анхны жагсаалт: {original_list}")
print(f"Урвуу жагсаалт: {reversed_list}")

# 23
def find_student_score(student_name, scores_dict):
    isFound = False
    for score in scores_dict.items():
        if student_name in score[0]:
            return score[1]
    if not isFound:
        return("Оюутан олдсонгүй")
scores = {"Болд": 85, "Сарнай": 92, "Дорж": 78}
print(f"Сарнайн дүн: {find_student_score('Сарнай', scores)}")
print(f"Нараагийн дүн: {find_student_score('Нараа', scores)}")

# 24
def generate_fibonacci(n):
    fibbonaci = [0, 1]
    for x in range(n - 2):
        fibbonaci.append((fibbonaci[-1]) + (fibbonaci[-2]))
    return fibbonaci
print(f"Фибоначчийн эхний 10 гишүүн: {generate_fibonacci(10)}")

# 25
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        try:
            return a / b
        except ZeroDivisionError:
            print("Алдаа: 0-д хуваах боломжгүй")
print(f"100 / 5 = {calculate(100, 5, '/')}")
print(f"30 * 3 = {calculate(30, 3, '*')}")
print(f"10 / 0 = {calculate(10, 0, '/')}")