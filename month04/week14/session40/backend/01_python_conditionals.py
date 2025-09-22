num = int(input("Нэг бүхэл тоо оруулна уу: "))
if num >= 0:
    print("Энэ бол эерэг тоо.")
else:
    print("Энэ бол сөрөг тоо.")
# 2
num = int(input("Таны насыг оруулна уу: "))
if num >= 18:
    print("Та насанд хүрсэн байна.")
else:
    print("Та насанд хүрээгүй байна.")

# 3
password = input("Нууц үгээ оруулна уу: ")
if password == "python123":
    print("Нууц үг зөв байна. Нэвтэрлээ.")
else:
    print("Нууц үг буруу байна. Хандах эрхгүй.")

# 4
num = int(input("Шалгах тоогоо оруулна уу: "))
if num % 2 == 0:
    print(f"{num} бол тэгш тоо.")
else:
    print(f"{num} бол сондгой тоо.")

# 5
num = int(input("Шалгалтын оноогоо оруулна уу: "))
if num >=60:
    print("Баяр хүргэе! Та тэнцсэн байна.")
else:
    print("Харамсалтай байна. Та тэнцээгүй.")

# 6
num = int(input("Агаарын хэмийг цельсээр оруулна уу: "))
if num <= 0:
    print("Ус хөлдөх цэгээс доош байна.")
else:
    print("Ус хөлдөх цэгээс доош ороогүй байна.")

# 7
word = input("Нэг үг бичнэ үү: ")
if len(word) > 8:
    print("Энэ бол урт үг юм байна.")
else:
    print("Энэ бол богино үг юм байна.")

# 8
num = int(input("Шалгах тоогоо оруулна уу: "))
if num == 0:
    print("Энэ тоо тэгтэй тэнцүү.")
elif num % 2 == 0:
    print(f"{num} бол тэгш тоо.")
else:
    print(f"{num} бол сондгой тоо.")
# 9
grade = int(input("Дүнгээ оруулна уу (0-100): "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# 10
workday = ["Даваа", "Мягмар", "Лхагва", "Пүрэв", "Баасан"]
holiday = ["Бямба", "Ням"]
day = input("Долоо хоногийн гаригийг оруулна уу: ")
if day in workday:
    print("Ажлын өдөр.")
else:
    print("Амралтын өдөр.")

# 11
username = input("Хэрэглэгчийн нэр: ")
password = input("Нууц үг: ")
if username == "admin" and password == "pass1234":
    print("Амжилттай нэвтэрлээ.")
else:
    print("Нэр эсвэл нууц үг буруу.")

# 12
vowels = ["а", "э", "и", "о", "ө", "ү"]
letter = input("Нэг үсэг оруулна уу: ").lower()
if letter in vowels:
    print(f"'{letter}' бол эгшиг.")
else:
    print(f"'{letter}' бол гийгүүлэгч.")

# 13
commands = ["улаан", "шар", "ногоон"]
command = input("Гэрлэн дохионы өнгийг оруулна уу (улаан, шар, ногоон): ")
if command not in commands:
    print("Буруу өнгө орууллаа.")
elif command == commands[0]:
    print("ЗОГС!")
elif command == commands[1]:
    print("БЭЛД!")
else:
    print("ЯВ!")

# 14
age = int(input("Насаа оруулна уу: "))
if age < 12:
    print("хүүхэд")
elif age < 19:
    print("өсвөр насныхан")
elif age < 65:
    print("насанд хүрэгч")
else:
    print("ахмад настан")

# 15
weight = float(input("Ачааны жинг (кг) оруулна уу: "))
if weight < 2:
    print(5000)
elif weight <= 10:
    print(15000)
else:
    print(30000)

# 16
character = input("Нэг тэмдэгт оруулна уу: ")
bool = character.isdigit()
if bool:
    print("Энэ бол тоо.")
else:
    print("Энэ бол тусгай тэмдэгт.")

# 17
year = int(input("Шалгах оноо оруулна уу: "))
if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"{year} он бол өндөр жил.") 
else:
    print(f"{year} он бол өндөр жил биш.")

# 18
age = int(input("Үзэгчийн насыг оруулна уу: "))
if age < 5:
    print(0)
elif age < 13:
    print(5000)
elif age < 65:
    print(10000)
else:
    print(7000)

# 19
firstnum = int(input("Эхний тоо: "))
action = input("Үйлдэл (+, -, *, /): ")
secondnum = int(input("Хоёр дахь тоо: "))
if action not in ("+", "-", "*", "/"):
    print("Буруу үйлдэл")
elif action == "/" and secondnum == 0:
    print("Алдаа: 0-д хувааж болохгүй.")
elif action == "+":
    print(firstnum + secondnum)
elif action == "-":
    print(firstnum - secondnum)
elif action == "*":
    print(firstnum * secondnum)
else:
    print(firstnum / secondnum)

# 20
side1 = int(input("1-р тал: "))
side2 = int(input("2-р тал: "))
side3 = int(input("3-р тал: "))
if side1 == side2 == side3:
    print("Адил талт гурвалжин.")
elif side1 in (side2, side3) or side2 in (side1, side3):
    print("Адил хажуут гурвалжин.")
else:
    print("Зөрөө талт гурвалжин.")

# 21
amount = int(input("Дүнгээ оруулна уу: "))
if amount > 100000:
    amount = amount * 0.9
    print(f"10% хөнгөлж, {amount}₮ боллоо.")
    havecard = input("Карттай юу? (тийм/үгүй): ")
    if havecard == "тийм":
        amount = amount*0.95
        print("Нэмэлт 5% хөнгөллөө.")
print(f"Эцсийн төлөх дүн: {amount}₮")

# 22
variations = ["хайч", "чулуу", "даавуу"]
player1 = input("1-р тоглогч (хайч, чулуу, даавуу): ")
player2 = input("2-р тоглогч (хайч, чулуу, даавуу):")
if player1 == player2:
    print("Тэнцлээ!")
elif player1 == "хайч" and player2 == "даавуу" or player1 == "даавуу" and player2 == "чулуу" or player1 =="чулуу" and player2 =="хайч":
    print("1-р тоглогч хожлоо!")
else:
    print("2-р тоглогч хожлоо!")

# 23
a = int(input("a коэффициент:"))
b = int(input("b коэффициент:"))
c = int(input("c коэффициент:"))
determinant = (b**2) - (4*a*c)
if determinant > 0:
    print("Тэгшитгэл 2 бодит шийдтэй.")
elif determinant == 0:
    print("Тэгшитгэл 1 бодит шийдтэй.")
else:
    print("Тэгшитгэл бодит шийдгүй.")

# 24
balance = 50000
action = input("Үйлдэл сонгоно уу (мөнгө авах / үлдэгдэл шалгах): ")
if action == "мөнгө авах":
    amount = int(input("Авах мөнгөн дүнгээ оруулна уу: "))
    balance -= amount
    print(f"Гүйлгээ амжилттай. Таны шинэ үлдэгдэл: {amount}₮")
elif action == "үлдэгдэл шалгах":
    print(f"Таны дансны үлдэгдэл: {amount}₮")
    
# 25
income = int(input("Таны жилийн орлого (төгрөгөөр): "))
score = int(input("Таны зээлийн түүхийн оноо (300-850):"))

if income > 50000000 and score > 700 or income > 80000000:
    print("Шалгуурт тэнцлээ. Танд зээл олгох боломжтой.")
else:
    print("Харамсалтай байна. Танд зээл олгох боломжгүй.")