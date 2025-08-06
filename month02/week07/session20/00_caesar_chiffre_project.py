def ceaser_cipher(text, key, direction):
    result = ''
    if direction == 'decrypt':
        key *= -1
    
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord("A")
            shifted_char_code = (ord(char) - start + key) % 26 + start
            result += chr(shifted_char_code)
        elif char.isdigit():
            shifted_char_code = (int(char) + key) % 10
            result += str(shifted_char_code)
        else:
            result += char
    return result

def main():
    print("Цезарийн шифр програмд тавтай морил!")
    direction = input("encrypt or decrypt : ")
    text = input("Enter your text : ")
    key = int(input("Enter your number : "))
    results = ceaser_cipher(text, key, direction)
    print(results)
if __name__ == '__main__':
    main()