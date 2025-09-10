# EX 1
def add_numbers(x, y):
    return x + y

result = add_numbers(10, 5)
print(f"Хоёр тооны нийлбэр: {result}")

# EX 2
def find_max(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max

my_list = [1, 9, 3, 22, 15]
max_value = find_max(my_list)
print(f"Жагсаалтын хамгийн их утга: {max_value}")

# EX 3
def get_string_length(string):
    return len(string)
length = get_string_length("Сайн байна уу?")
print(f"Тэмдэгт мөрийн урт: {length}")

# EX 4
def filter_even_numbers(list):
    return [x for x in list if x % 2 == 0]
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter_even_numbers(original_list)
print(f"Тэгш тоонууд: {evens}")

# EX 5
def total_characters(words):
    total = 0
    for item in words:
        total += len(item)
    return total
words = ["Python", "бол", "хялбар"]
total_len = total_characters(words)
print(f"Нийт тэмдэгтийн тоо: {total_len}")

# EX 6
def print_movie_details(movies):
    return print(f"Нэр: {movies.get('title')}, Он: {movies.get('year')}, Найруулагч: {movies.get('director')}")
movie_data = {'title': 'Inception', 'year': 2010, 'director':
'Christopher Nolan'}
print_movie_details(movie_data)

# EX 7
def find_movies_by_year(movies, year):
    themovies = []
    for movie in movies:
        if movie.get('year') == year:
            themovies.append(movie.get('title'))
    return themovies
movie_list = [
{'title': 'Inception', 'year': 2010},
{'title': 'The Dark Knight', 'year': 2008},
{'title': 'Interstellar', 'year': 2014},
{'title': 'The Prestige', 'year': 2006}
]
movies_2010 = find_movies_by_year(movie_list, 2010)
print(f"2010 онд гарсан кинонууд: {movies_2010}")

# EX 8
def calculate_average(scores):
    return sum(scores)/len(scores)
scores = [80, 95, 88, 79, 92]
average_score = calculate_average(scores)
print(f"Дундаж оноо: {average_score}")

# EX 9
def count_word_frequency(text):
    words_counts = {}
    text_list = text.lower().split(" ")
    for item in text_list:
        if item in words_counts:
            words_counts[item] += 1
        else:
            words_counts[item] = 1
    return words_counts
text = "Энэ бол дасгал мөн энэ бол сайн дасгал"
word_counts = count_word_frequency(text)
print(f"Үгийн давтамж: {word_counts}")

# EX 10
def find_top_spender(customer_data):
    max = 0
    name = ""
    for data in customer_data:
        if data.get('spent') > max:
            max = data.get('spent')
            name = data.get('name')
    return name
customer_data = [
{'name': 'Болд', 'spent': 150},
{'name': 'Дорж', 'spent': 250},
{'name': 'Тулга', 'spent': 90}
]
top_spender_name = find_top_spender(customer_data)
print(f"Хамгийн их зарцуулсан хэрэглэгч: {top_spender_name}")