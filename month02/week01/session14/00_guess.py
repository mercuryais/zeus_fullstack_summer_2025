import random

number = random.randint(0, 100)
guess = int(input("Toogoo oruulna uu! : "))
while guess < 100 or guess > 0:

    if guess == number:
        print("Ta zov taalaa")
        break
    elif number < guess:
        guess = int(input("pick lower number : "))
    else:
        guess = int(input("pick higher number : "))

