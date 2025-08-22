import psycopg2
from psycopg2 import OperationalError 

def connect_db():
    try:
        conn = psycopg2.connect( 
            dbname="student_register",
            user="postgres",
            password="",
            host="localhost",
            port="5433"
        )
        return conn
    except OperationalError as e:
        print(f"Холболтын алдаа гарлаа: {e}")
        return None
def add_student(conn):
    try:
        ovog_ner = input("Оюутны овог нэрийг оруулна уу: ")
        email = input("И-мэйл хаягийг оруулна уу: ")
        utas = input("Утасны дугаарыг оруулна уу: ")
        cur = conn.cursor()
        query = """
            INSERT INTO students(ovog_ner, email, utas)
            VALUES(%s, %s, %s)
        """
        cur.execute(query, (ovog_ner, email, utas))
        conn.commit()
        print(f"'{ovog_ner}' амжилттай бүртгэгдлээ.")
        cur.close()
    except Exception as e:
        print(f"Оюутан нэмэхэд алдаа гарлаа: {e}")
        conn.rollback()
def view_students(conn):
    try:
        cur = conn.cursor()
        SELECT_STUDENTS = """
            SELECT * FROM students
        """
        cur.execute(SELECT_STUDENTS)
        rows = cur.fetchall()
        if not rows:
            print("Бүртгэлтэй оюутан байхгүй байна.")
            return
        print("\n--- Бүртгэлтэй оюутнууд ---")
        print(f"{'ID':<5} {'Овог нэр':<25} {'И-мэйл':<30} {'Утас':<15}")
        print("-" * 75)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<30} {row[3]:<15}")
        print("-" * 75)
        cur.close()
    except Exception as e:
        print(f"Мэдээлэл харахад алдаа гарлаа: {e}")
def main():
    conn = connect_db()
    if conn is None:
        return
    while True:
        print("\n===== Оюутны Бүртгэлийн Систем =====")
        print("1. Шинэ оюутан нэмэх")
        print("2. Бүх оюутныг харах")
        print("3. Гарах")
        choice = input("Сонголтоо оруулна уу (1-3): ")
        if choice == '1':
            add_student(conn)
        elif choice == '2':
            view_students(conn)
        elif choice == '3':
            print("Програмаас гарлаа.")
            break
        else:
            print("Буруу сонголт. 1-3 хооронд сонгоно уу.")
    if conn:
        conn.close()

if __name__ == "__main__":
    main()

