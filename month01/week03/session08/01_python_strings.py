# Python Strings
# REPL (Read Evaluate Print Loop)
a = 100
b = 10.5
c = "110"

# Type
print(type(a))
print(type(b))
print(type(c))

# Python Strings
fred = "Why do gorillas have big nostrils? Big Fingers!!"
print(fred)
print(type(fred))
fred = "What is pink and fluffy? Pink Fluff!!"

# Error code
fred = "How do dinosours pay their bills?"

# ''' '''
fred = '''
        How do dinosaurs pay their bills?
        With tyrannosaurs checks
    '''
# Handling Problems with String
silly_string = '''He said, "Arent't can't shouldn't woudln't."'''
print(silly_string)

# Special character
single_quote_str = "He said, \"Aren\'t can\'t shoudn\'t woudln\'t.\""
print(single_quote_str)

# Embedding Values in Strings
# F-string python
my_score = 1000
message = f'I scored {my_score} points'
print(message)

# Example 01
first = 0 
second = 8
print(f'What did the number {first} say to the number {second}? Nice belt!!')

# Example 02
print(f"Two plus two equals {2 + 2}")

# Multiplying Strings
print(10 * 'a')
spaces = ' ' * 25
#String indexeer character awah
word = 'Zeus are pythonistas. Great!!!'
print(word[0])
print(word[0], word[1], word[2], word[3])
print(word[0:4])
print(len(word))