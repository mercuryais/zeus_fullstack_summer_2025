# X 01

x = 0
while x < 20:
    print(f'hello {x}')
    if x < 9:
        break

# X 02

age = int(input("Tanii nas hed ve? "))
l = 0

while l <= age:

    if l % 2 ==0:
        print(l)

    l = l + 1
        
# X 03

weightE = int(input("Tanii jin hed ve? "))
loop = 1

while loop < 16:

    weightM = weightE * 0.165
    print(f"Tanii saran deerh jin {loop} dugaar jild {weightM}kg")
    loop = loop + 1
    weightE = weightE + 2