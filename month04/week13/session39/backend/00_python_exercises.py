import datetime
# 1
print("Сайн уу, Python!")
# 2
ner = 'Batsuuri'
print(f"Сайн уу, {ner}")
# 3
ognoo = 19
sar = 9
jil = 2025
print(f"{jil} оны {sar}-р сарын {ognoo}")
# 4
durtai_ishlel = "Мэдэхгүйгээ мэднэ гэдэг мэргэн ухааны эхлэл."
print(durtai_ishlel)
# 5
ner = 'Batsuuri'
ovog = 'Ayurzana'
print(ner, ovog)
# 6
ner = input("Таны нэр хэн бэ? ").capitalize()
print(f"Сайн уу, {ner}!")
# 7
favcol = input("Таны дуртай өнгө юу вэ?").capitalize()
print(f"Таны дуртай өнгө бол {favcol} юм байна.")
# 8
city = input("Та аль хотод төрсөн бэ? ").capitalize()
print(f"Та {city} хотод төрсөн юм байна.")
# 9
ovog = input("Таны овог хэн бэ ? ").capitalize()
ner = input("Таны нэр хэн бэ ? ").capitalize()
print(f"Таны овог: {ovog}")
print(f"Таны нэр: {ner}")
print(f"Таны бүтэн нэр: {ovog} {ner}")
# 10
favbook = input("Таны дуртай ном юу вэ? ")
print("Надад ч гэсэн {favbook} таалагддаг.")
# 11
pet = input("Таны гэрийн тэжээвэр амьтны нэр юу вэ? ")
print(f"Сайн уу, {pet}! Чи сайн амьтан шүү.")
# 12
wsh = input("Таны мөрөөдлийн ажил юу вэ? ")
print(f"Та ирээдүйд мундаг {wsh} болох болно!")
# 13
favfood = input("Таны дуртай хоол юу вэ? ")
print(f"Тантай адилхан, надад ч гэсэн {favfood} таалагддаг.")
# 14
country = input("Улсын нэр оруулна уу: ").capitalize()
city = input(f"{country} улсын нийслэлийн нэрийг оруулна уу: ").capitalize()
print(f"{country}-ын нийслэл бол {city}.")
# 15
favmov = input("Таны дуртай киноны нэр: ")
print(f"{favmov} бол гоё кино!")
# 16
num = int(input("Нэг тоо оруулна уу: "))
print(f"Таны оруулсан тоог 2-оор үржүүлэхэд {num * 2} гарна.")
# 17
num1 = int(input("Эхний тоог оруул: "))
num2 = int(input("Хоёр дахь тоог оруул: "))
print(f"Хоёр тооны нийлбэр: {num1+num2}")
# 18
num1 = int(input("Эхний тоог оруул: "))
num2 = int(input("Хоёр дахь тоог оруул: "))
print(f"Хоёр тооны ялгавар: {num1-num2}")
# 19
num1 = int(input("Эхний тоог оруул: "))
num2 = int(input("Хоёр дахь тоог оруул: "))
print(f"Хоёр тооны үржвэр: {num1*num2}")
# 20
num1 = int(input("Эхний тоог оруул: "))
num2 = int(input("Хоёр дахь тоог оруул: "))
print(f"Хоёр тооны ноогдвор: {num1/num2}")
# 21
borndate = int(input("Та хэдэн онд төрсөн бэ?"))
print(f"Та ойролцоогоор {2025-borndate} настай юм байна.")
# 22
length = int(input("Квадратын талын уртыг оруулна уу: "))
print(f"Квадратын периметр: {length*4}")
# 23
length = int(input("Квадратын талын уртыг оруулна уу: "))
print(f"Талын урт нь {length} байх квадратын талбай нь: {length**2}")
# 24
suuri = int(input("Гурвалжны суурийг оруулна уу: "))
ondor = int(input("Гурвалжны өндрийг оруулна уу: "))
print(f"Энэхүү гурвалжны талбай нь: {suuri*ondor}")
# 25
too = float(input("Нэг бутархай тоо оруулна уу: "))
hariu = too / 2
print(f"{too} тоог 2-т хуваахад {hariu} гарна.")
# 26 
too = float(input("Эхний бутархай тоо оруулна уу: "))
too2 = float(input("Хоёр дахь бутархай тоо оруулна уу: "))
print(f"Хоёр бутархай тооны нийлбэр: {too+ too2}")
# 27
c = float(input("Цельсийн хэмийг оруулна уу: "))
print(f"{c}°C нь {c * 9/5 + 32} °F-тэй тэнцүү.")
# 28
age = int(input("Та одоо хэдэн настай вэ? "))
print(f"Та 10 жилийн дараа {age + 10} настай байх болно.")
# 29
score1 = int(input("1-р шалгалтын оноо: "))
score2 = int(input("2-р шалгалтын оноо: "))
score3 = int(input("3-р шалгалтын оноо: "))
print(f"Таны 3 шалгалтын нийт оноо: {sum(score1, score2, score3)}")
# 30
price = float(input("Барааны нийт үнийн дүнг оруулна уу: "))
prepaid = float(input("Урьдчилж төлсөн дүнг оруулна уу: "))
print(f"Таны үлдэгдэл төлбөр: {price-prepaid}")
# 31
name = input("Таны нэр: ")
age = int(input("Таны нас: "))
print(f"{name} нь {age} настай.")
# 32
proname = input("Барааны нэр: ")
price = int(input("Нэгжийн үнэ: "))
quantity = int(input("Тоо ширхэг: "))
print(f"{proname} барааны нийт үнэ: {price*quantity}")
# 33
boy = int(input("Ангид хэдэн хүү байдаг вэ? "))
girl = int(input("Ангид хэдэн охин байдаг вэ?"))
print(f"Энэ ангид нийт {boy+girl} сурагчтай.")
# 34
height = float(input("Таны өндөр (метрээр): "))
weight = float(input("Таны жин (килограммаар): "))
print(f"Таны өндөр {height}, жин {weight}кг байна.")
# 35
brand = input("Таны машины брэнд:")
date = int(input("Үйлдвэрлэсэн он: "))
print(f"Та {date} онд үйлдвэрлэсэн {brand} машинтай юм байна.")
# 36
city = input("Та аль хот руу аялах вэ?")
duration = int(input("Та хэдэн хоног аялах вэ? "))
print(f"Та {city} хот руу {duration} хоног аялах гэж байгаа юм байна. Сайхан аялаарай!")
# 37
number = int(input("Утасны дугаараа оруулна уу: "))
print(f"Таны дугаар: {number}")
# 38
radius = float(input("Тойргийн радиусыг оруулна уу: "))
print(f"Радиус нь {radius} байх тойргийн талбай ойролцоогоор {radius*3.14} байна.")
# 39
balance = float(input("Таны дансанд одоо хэдэн төгрөг байгаа вэ? "))
income = float(input("Нэмж орсон орлогын дүнгээ оруулна уу: "))
print(f"Таны дансны нийт үлдэгдэл: {balance+income}₮ боллоо.")
# 40
apple = int(input("Та хэдэн ширхэг алим авсан бэ? "))
orange = int(input("Та хэдэн ширхэг жүрж авсан бэ? "))
print(f"Та нийт {apple+orange} ширхэг жимс авсан байна.")
# 41
x = datetime.datetime.now()
ovog = input("Таны овог: ")
year = int(input("Таны төрсөн он: "))
print(f"Эрхэм {name}-нхон та ойролцоогоор {x-year} настай юм байна.")
# 42
length = float(input("Өрөөний уртыг (метрээр) оруулна уу: "))
width = float(input("Өрөөний өргөнийг (метрээр) оруулна уу: "))
print(f"Өрөөний нийт талбай: {length*width}м.кв.")
# 43
sport = input("Та ямар спортод дуртай вэ? ")
duration = int(input(f"Та {sport}-өөр хэдэн жил хичээллэж байна вэ? 10"))
print(f"Та {sport}-өөр {duration} жил хичээллэсэн гэдэг үнэхээр мундаг!")
# 44
price = float(input("Нэг хуудас хэвлүүлэх үнэ: "))
quantity = int(input("Хэдэн хуудас хэвлүүлэх вэ? "))
print(f"Нийт төлбөр: {price*quantity}₮ болно.")
# 45
name = input("Нэр: ")
email = input("Имэйл хаяг: ")
phone = int(input("Утасны дугаар: "))
print(f"Нэр: {name}")
print(f"Имэйл хаяг: {email}")
print(f"Утасны дугаар: {phone}")
# 46
animal = input("Таны дуртай амьтан юу вэ? ")
sound = input(f"{animal} ямар дуу гаргадаг вэ? ")
print(f"{animal} нь {sound} гэж дуугардаг.")
# 47
word = input("Нэг үг оруулна уу: ")
print(word, word, word)
# 49
name = input("Таны нэр: ")
friend = input("Таны найзын нэр: ")
print(f"{name} ба {friend} бол сайн найзууд.")
# 50
word = input("Таны дуртай монгол үг юу вэ? ")
print(f"Таны дуртай үг бол '{word}' юм байна. Сайхан сонголт!")