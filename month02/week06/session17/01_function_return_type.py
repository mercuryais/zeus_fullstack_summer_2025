def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(5,6))
result_01 = add_two_numbers(11,12)
print(result_01)


#RETURN MANY VALUES
def get_user_info():
    name = 'Alice'
    age = 13
    return name, age

user_name, user_age = get_user_info()
print(f"Name: {user_name}, Age: {user_age}")