# Object Oriented Programming in Python
# Python Class
# Atrribute of class
class Human:
    body = 1
    height = 1.75
    eyes = 2
    name = 'Human'
    skin_color = 'Biege'
    is_single = True

boldoo = Human()
print(boldoo)

boldoo.name = "Boldoo"

# init method
# class metohod - function in class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

bulldog = Dog("Bulldog", 2)
bankhar = Dog("Mongol Bankhar", 4)
print(boldoo.body)

class Cat:
    def __init__(self, age, species):
        self.age = age
        self.specfies = species
cat1 = Cat(23, "Felis")
print(cat1.age, cat1.specfies)

class Car():
    def __init__(self, wheel, brand, engine, style):
        self.wheel = wheel
        self.brand = brand
        self.engine = engine
        self.style = style
volkswagen = Car(4, "Volkswagen", "Benzine", "Lux")
motorcycle = Car(2, "random", "Random", "SPooort")
audi = Car(4, "Something", "Idk", "dc")

class Animal:
    species = "Animalus"
    is_mammal = False
    def __init__(self, age, leg, eats_plant):
        self.age = age
        self.leg = leg
        self.eats_plant = eats_plant
    def __str__(self):
        return f"Hello , {self.eats_plant}"
wolf = Animal(2, 4, False)
wolf.is_mammal = True
elephant = Animal(40, 4, True)
elephant.is_mammal= True
print(wolf)

# EX 01
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title}, {self. author},{self.pages}"
my_book = Book("The hobbit", "jrr", 310)
print(my_book)

# EX 02
class Student:
    student_count = 0
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"{self.name}, {self.grade} Grade, {self.student_count} Students"
student1 = Student("Alice", "10th")
student2 = Student("Bob", "11th")
student3 = Student("Charlie", "9th")
Student.student_count = 3
print(student1)