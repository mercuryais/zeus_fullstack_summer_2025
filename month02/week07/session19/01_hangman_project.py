import random # exercise with dictionary kwargs
def get_word(): #  exercise with file handling
    words = ["other", #
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
#    displayed = ""
#    for letter in word:
#        if letter in guessed_letters:
#            displayed += letter
#        else:
#            displayed += "_"
#    return displayed.strip()
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = get_word()
    guessed_letters = []
    failed = []
    attempts = 6
    print("Тавтай морилно уу, Үг Таах Тоглоомд!")
    print("Үгийг таана уу. Та 6 оролдлоготой.")
    while attempts:
        print(display_word(word_to_guess,guessed_letters))
        guess = input("Enter a letter : ")
        if len(guess) > 1 or not guess.isalpha():
            print("Enter only 1 letter at a time! ")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        if guess in word_to_guess:
            guessed_letters.append(guess)
        attempts -= 1
        print("Left attempts : ", attempts)
        if display_word(word_to_guess, guessed_letters) == word_to_guess:
            print("Congratulations!")
            break
    if not attempts:
        print("You are out of attemps!")
if __name__ == "__main__":
    hangman()


    # guessed letter dee bolzol hangasan utgiig garaas awaad word d baiga buhletter baih ym bol tegel bolo