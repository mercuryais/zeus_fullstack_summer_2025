import psycopg2

connection = psycopg2.connect(
dbname="coffee_machine",
user="postgres",
password="",
host="localhost",
port="5433"
)
cur = connection.cursor()

def get_resources():
    cur.execute("SELECT water, milk, coffee, money FROM resources WHERE id=1;")
    return cur.fetchone()
def update_resources(new_water, new_milk, new_coffee, new_money):
    cur.execute("""
        UPDATE resources
        SET water=%s, milk=%s, coffee=%s, money=%s
        WHERE id=1;
    """, (new_water, new_milk, new_coffee, new_money))
    connection.commit()

def get_drink(name):
    cur.execute("SELECT water, milk, coffee, cost FROM menu WHERE name=%s;", (name,))
    return cur.fetchone()

def report():
    water, milk, coffee, money = get_resources()
    print(f"Ус: {water}ml")
    print(f"Сүү: {milk}ml")
    print(f"Кофе: {coffee}g")
    print(f"Мөнгө: ${money}")

def is_resource_sufficient(drink):
    water, milk, coffee, _ = get_resources()
    d_water, d_milk, d_coffee, _ = drink

    if water < d_water:
        print("Уучлаарай, ус хүрэлцэхгүй байна.")
        return False
    if milk < d_milk:
        print("Уучлаарай, сүү хүрэлцэхгүй байна.")
        return False
    if coffee < d_coffee:
        print("Уучлаарай, кофе хүрэлцэхгүй байна.")
        return False
    return True

def process_coins():
    print("Зоос хийж өгнө үү.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("Hpw many pennies?: ")) * 0.01
    return total

def is_transactioln_successful(money_received, drink_cost):
    water, milk, coffee, current_money = get_resources()
    if money_received >= drink_cost:
        change = round(money_received - float(drink_cost), 2)
        if change > 0:
            print(f"Таны хариулт ${change}.")
        update_resources(water, milk, coffee, float(current_money) + float(drink_cost))
        return True
    else:
        print("Уучлаарай, мөнгө хүрэлцэхгүй байна,. Мөнгө буцаан олголоо.")
        return False

def make_coffee(drink_name, drink):
    d_water, d_milk, d_coffee, _ = drink
    water, milk, coffee, money = get_resources()
    
    update_resources(
        water - d_water,
        milk - d_milk,
        coffee - d_coffee,
        money
    )

    print(f"Таны {drink_name} бэлэн боллоо. Амттай уу")

machine_on = True

while machine_on:
    choice = input("Та юу уухыг хүсэж байна? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        drink = get_drink(choice)
        if drink:
            if is_resource_sufficient(drink):
                payment = process_coins()
                if is_transactioln_successful(payment, drink[3]):
                    make_coffee(choice, drink)
        else:
            print("Буруу сонголт. Дахин оролдоно уу.")
cur.close()
connection.close()