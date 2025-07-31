import random

passwd = []
letters = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lenghtQ = int(input("Ta nuuts ugend heden useg bailgahiig husej baina ve?"))
symbolsQ = int(input("Ta heden symbol oruulahiig husej baina ve?"))
numbersQ = int(input("Ta heden too oruulahiig husej baina ve?"))

for _ in range(lenghtQ):
    vassal = random.choice(letters)
    passwd.append(vassal)

for _ in range(symbolsQ):
    vassal = random.choice(symbols)
    passwd.append(vassal)

for _ in range(numbersQ):
    vassal = random.choice(numbers)
    passwd.append(vassal)

random.shuffle(passwd)
vassal = "".join(passwd)
print(vassal)

# WHAT IS THE DIFFERENCE BETWEEN CHOICES AND CHOICE