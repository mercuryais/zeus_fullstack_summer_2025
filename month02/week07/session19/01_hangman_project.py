import random
def get_word():
    words = ["other", 
                "press",
                "account",
                "lot",
                "sofa",
                "think",
                "appointment",
                "provide",
                "mist",
                "pull"]
    return random.choice(words)
    
def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = get_word()
    guessed_letters = []
    attempts = 6
    print("Тавтай морилно уу, Үг Таах Тоглоомд!")
    print("Үгийг таана уу. Та 6 оролдлоготой.")
    while attempts:
        print(display_word(word_to_guess, guessed_letters))
        print("====================")
        guess = input("Enter you guess : ")
        if len(guess) != 1:
            print("Please enter one letter at a time.")
            continue
        elif not guess.isalpha():
            print("Please only enter alphabet.")
            continue
        elif guess in guessed_letters:
            print("You already tried this letter.")
            continue
        else:
            guessed_letters.append(guess)
            if display_word(word_to_guess, guessed_letters) == word_to_guess:
                print("You won!")
                break
            elif guess in word_to_guess:
                print("Correct!\nAttempts left : ", attempts)
            else:
                attempts -= 1
                print("Incorrect!\nAttempts left : ", attempts)
    if not attempts:           
        print("You lose!")
if __name__ == "__main__":
    hangman()
