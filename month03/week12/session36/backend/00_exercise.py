import math
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_method(self):
        print(f"Brand is {self.brand}, model is {self.model}")
myCar = Car("Toyota", "Prius")
myCar.show_method()

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

class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
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

