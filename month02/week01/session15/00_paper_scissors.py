import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
game_images = [rock, paper, scissors]

picked = int(input("Rock paper scissors! : "))

if picked < 0:
    print("Ta buruu dugaar oruulsan baina")

elif picked > 2:
    print("Ta buruu dugaar oruulsan baina")

else:
    randomNumber = random.randint(0, 2)
    bot = game_images[randomNumber]
    print(game_images[picked])
    print(game_images[randomNumber])

    if picked - randomNumber == 1 or picked - randomNumber == -2:
        print("You won!")
    elif picked - randomNumber == 0:
        print("Its a draw")

    else:
        print("You lose!")



