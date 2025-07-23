import random

def guess_the_number():  # function
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    secret_number  = random.randint(1, 100)
    attempts = 0
    guess = 0

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess> secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations!. You guessed the number {secret_number} in {attempts} attemps.")
            
guess_the_number()