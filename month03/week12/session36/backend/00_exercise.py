import math

# EX 1
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_method(self):
        print(f"Brand is {self.brand}, model is {self.model}")
myCar = Car("Toyota", "Prius")
myCar.show_method()

# EX 2
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def isAdult(self):
        if self.age < 18:
            return "Underage"
        else:
            return "Adult"
student1 = Student("Болд", 20)
student2 = Student("Дорж", 17)
print(f"{student1.name} насанд хүрсэн үү? {student1.isAdult()}")
print(f"{student2.name} насанд хүрсэн үү? {student2.isAdult()}")

# EX 3
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return (self.radius**2) * 3.14
    def calculate_circumference(self):
        return self.radius * 2 * 3.14
circle = Circle(5)
print(f"5 радиустай тойргийн талбай: {circle.calculate_area():.2f}")
print(f"5 радиустай тойргийн урт: {circle.calculate_circumference():.2f}")

# EX 4
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    def __str__(self):
        return f"Данс эзэмшигч: {self.owner_name}, Үлдэгдэл: {self.balance} төгрөг"
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} төгрөг нэмэгдлээ. Одоогийн үлдэгдэл: {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} төгрөг татлаа. Одоогийн үлдэгдэл: {self.balance}")
        else:
            print("Гүйлгээ амжилтгүй. Таны үлдэгдэл хүрэлцэхгүй байна.")
acc = BankAccount("Цэцэг", 50000)
acc.deposit(20000)
acc.withdraw(60000)
acc.withdraw(20000)

# EX 5
acc1 = BankAccount("Баяр", 20000)
print(acc1)

# EX 6
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by '{book.author}' номыг санд нэмлээ.")
    def list_books(self):
        print("--- Номын сангийн номнууд ---")
        for book in self.books:
            print(f"{book.title} by {book.author}")

book1 = Book("Тунгалаг тамир", "Ч.Лодойдамба")
book2 = Book("Leaders Eat Last", "Simon Sinek")
library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()

# EX 7
class ShopItem:
    tax_rate = 0.1 
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    def get_total_price(self):
        return self.price * 1.1
item1 = ShopItem("Талх", 2000)
item2 = ShopItem("Сүү", 3500)
print(f"{item1.name}-ийн нийт үнэ: {item1.get_total_price()}")
print(f"{item2.name}-ийн нийт үнэ: {item2.get_total_price()}")

# EX 8
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Hav Hav!")
class Cat(Animal):
    def speak(self):
        print("Miav!")
my_dog = Dog()
my_cat = Cat()
my_dog.speak()
my_cat.speak()

#  EX 9
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary 
    def show_details(self):
        print(f"Ажилтан: {self.name}, Нас: {self.age}, ID: {self.employee_id}, Цалин: {self.salary}")
emp = Employee("Сарнай", 30, "E123", 2500000)
emp.show_details()

# EX 10
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other_point):
        a = (other_point.x - self.x)**2
        b = (other_point.y - self.y)**2
        return math.sqrt(a+b)
p1 = Point(1, 2)
p2 = Point(4, 6)
distance = p1.distance_to(p2)
print(f"p1(1,2) ба p2(4,6) цэгүүдийн хоорондох зай: {distance:.2f}")