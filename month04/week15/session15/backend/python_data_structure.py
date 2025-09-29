def filter_even_numbers(number_list):
    evens = []
    for number in number_list:
        if number % 2 == 0:
            evens.append(number)
    return evens
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(my_numbers)
print(f"Анхны жагсаалт: {my_numbers}")
print(f"Шүүсэн жагсаалт: {evens}")

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements
list_a = [1, 2, 3, 4, 5, "алим"]
list_b = [4, 5, 6, 7, 8, "алим"]
commons = find_common_elements(list_a, list_b)
print(f"Ерөнхий элементүүд: {commons}")

def word_length_dict(word_list):
    result_dict = {}
    for item in word_list:
        result_dict.update({item : len(item)})
    return result_dict
words = ["python", "програм", "өгөгдөл", "бүтэц"]
lengths = word_length_dict(words)
print(lengths)

def get_grade_status(scores_dict):
    status_dict = {}
    for item in scores_dict.items():
        if item[1] > 60:
            status_dict.update({item[0] : "Pass"})
        else:
            status_dict.update({item[0] : "Fail"})
    return status_dict
scores = {"Болд": 85, "Сарнай": 92, "Дорж": 58, "Нараа": 77}
statuses = get_grade_status(scores)
print(statuses)

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for item in dict2.items():
        merged.update({item[0] : item[1]})
    return merged
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'd': 40}
result = merge_dicts(d1, d2)
print(f"Нэгтгэсэн толь бичиг: {result}")

def most_frequent_char(text):
    counts = {}
    for char in text:
        if char in counts:
            num = counts.get(char)
            num += 1
            counts.update({char : num})
        else:
            counts.update({char : 1})
    max = 0
    maxchar = ""
    for item in counts.items():
        if item[1] > max:
            maxchar = item[0]
            max = item[1]
    return maxchar
my_text = "програмчлалын үндсэн ойлголтууд"
print(f"Хамгийн олон орсон тэмдэгт: '{most_frequent_char(my_text)}'")

def add_contact(book, name, phone):
    book.update({name : phone})
def find_contact(book, name): 
    if name in book:
        for item in book.items():
            if item[0] == name:
                return item
    else:
        return
contact_book = {}
add_contact(contact_book, "Болд", "9911XXXX")
add_contact(contact_book, "Сарнай", "9988XXXX")
found = find_contact(contact_book, "Сарнай")
if found:
    print(f"Олдсон: {found}")
else:
    print("Контакт олдсонгүй.")

def calculate_total(cart, prices):
    total_price = 0
    for item in cart:
        if item in prices:
            total_price += prices.get(item)
        else:
            print(f"Анхааруулга: '{item}' бараа олдсонгүй.")
    return total_price
available_items = {"алим": 3000, "талх": 1800, "сүү": 3500, "өндөг": 450}
shopping_cart = ["алим", "талх", "сүү", "алим", "тараг"]
total = calculate_total(shopping_cart, available_items)
print(f"Төлөх нийт дүн: {total}₮")

def invert_dict(d):
    inverted = {}
    for item in d.items():
        inverted.update({item[1] : item[0]})
    return inverted
original_dict = {"нэр": "Болд", "мэргэжил": "программист", "хот":
"Улаанбаатар"}
inverted = invert_dict(original_dict)
print(f"Анхны толь бичиг: {original_dict}")
print(f"Урвуулсан толь бичиг: {inverted}")

def calculate_averages(students_data):
    averages = {}
    for item in students_data.items():
        score = 0
        count = 0
        for a in item[1].items():
            score += a[1]
            count += 1
        averages.update({item[0] : score/count})
    return averages
student_grades = {
"Болд": {"Математик": 85, "Физик": 92, "Англи хэл": 78},
"Сарнай": {"Математик": 95, "Физик": 90, "Англи хэл": 97}
}
avg_scores = calculate_averages(student_grades)
print(f"Оюутнуудын дүнгийн дундаж: {avg_scores}")