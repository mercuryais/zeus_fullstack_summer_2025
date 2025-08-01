import random

scores = []

for score in range(51):
    x = random.randint(0, 100)
    scores.append(x)
print(max(scores))