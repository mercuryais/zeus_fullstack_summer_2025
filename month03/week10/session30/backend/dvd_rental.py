import psycopg2
INSERT_TABLE = """
    INSERT INTO actor (first_name, last_name)
    VALUES(%s, %s)
"""
def connect():
    return psycopg2.connect(
    dbname="dvd_rental", 
    user="postgres",
    password="", 
    host="localhost",
    port="5433"
    )
def show_table(table_name):
    conn = connect()
    cur = conn.cursor()
    try:
        sql =f'SELECT * FROM {table_name} order by {table_name}_id desc limit 5;'
        cur.execute(sql)
        rows = cur.fetchall()
        print(f"\n==== {table_name.upper()} хүснэгт (эхний 5 мөр) ====")
        for row in rows:
            print(row)
    except Exception as e:
        print("⚠Алдаа:", e)
    finally:
        cur.close()
        conn.close()
def insert_actor():
    conn = connect()
    cur = conn.cursor()
    try:
        first = input("Жүжигчний нэр (first_name): ")
        last = input("Жүжигчний овог (last_name): ")
        cur.execute(INSERT_TABLE, (first, last))
        conn.commit()
        print("✅ Жүжигчинг амжилттай нэмлээ!")
    except Exception as e:
        print("⚠Алдаа:", e)
    finally:
        cur.close()
        conn.close()
def main_menu():
    while True:
        print("\n=== DVD Rental App ===")
        print("1. Actor хүснэгт харуулах")
        print("2. Film хүснэгт харуулах")
        print("3. Customer хүснэгт харуулах")
        print("4. Actor хүснэгтэд шинэ өгөгдөл нэмэх")
        print("0. Гарах")
        choice = input("Сонголтоо оруулна уу: ")
        if choice == "1":
            show_table("actor")
        elif choice == "2":
            show_table("film")
        elif choice == "3":
            show_table("customer")
        elif choice == "4":
            insert_actor()
        elif choice == "0":
            print("👋 Програм дууслаа.")
            break
        else:
            print("⚠Буруу сонголт, дахин оролдоно уу.")
if __name__ == "__main__":
    main_menu()