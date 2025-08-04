import random
# 1
score = [random.randint(0, 100) for _ in range(0, 50)]
# 2
print(max(score))       
# 3
squares = [x**2 for x in range(11)]
print(squares)
# 4
even = [x for x in range(21) if x % 2 == 0]
print(even)
# 5
the_words = ["cat", "window", "python"]
words = [len(word) for word  in the_words]
print(words)
# 6
upper = ["HELLO", "WORLD", "PYTHON"]
lower = [word.lower() for word in upper]
print(lower)
# 7
words = ["hi", "hello", "to", "world", "on"]
long = [three for three in words if len(three) > 2]
print(long)
