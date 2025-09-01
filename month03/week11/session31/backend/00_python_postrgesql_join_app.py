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
def view_courses(conn):
    try:
        cur = conn.cursor()
        print("\n--- Боломжит хичээлүүд ---")
        select_course = """
        select * from courses
        """
        cur.execute(select_course)
        courses = cur.fetchall()
        for course in courses:
            print(f"[{course[0]}] {course[1]}")
        print("-" * 28)
        cur.close()
        return courses
    except Exception as e:
        print(f"Хичээл харахад алдаа гарлаа: {e}")
        return []
def add_student(conn):
    courses = view_courses(conn)
    if not courses:
        print("Нэмэх боломжтой хичээл олдсонгүй. Эхлээд хичээл нэмнэ үү.")
        return
    try:
        ovog_ner = input("Оюутны овог нэрийг оруулна уу: ")
        email = input("И-мэйл хаягийг оруулна уу: ")
        utas = input("Утасны дугаарыг оруулна уу: ")
        while True:
            course_id = input("Хичээлийн ID-г сонгоно уу: ")
            if course_id.isdigit() and any(int(course_id) == c[0] for c in
            courses):
                break
            else:
                print("Буруу ID байна. Дээрх жагсаалтаас сонгоно уу.")
        cur = conn.cursor()
        add_sql = """
        insert into students (ovog_ner, email, utas, course_id)
        values (%s, %s, %s, %s)
        """
        cur.execute(add_sql, (ovog_ner, email, utas, course_id))
        conn.commit()
        print(f"'{ovog_ner}' амжилттай бүртгэгдлээ.")
        cur.close()
    except Exception as e:
        print(f"Оюутан нэмэхэд алдаа гарлаа: {e}")
        conn.rollback()
def view_students_with_courses(conn):
    try:
        cur = conn.cursor()
        left_join_sql = """
        select s.id, s.ovog_ner, s.email, c.course_name
        from students s
        left join courses c on s.course_id = c.id
        """
        cur.execute(left_join_sql)
        rows = cur.fetchall()
        if not rows:
            print("Бүртгэлтэй оюутан байхгүй байна.")
            return
        print("\n--- Оюутнууд ба Тэдний Хичээлүүд ---")
        print(f"{'ID':<5} {'Овог нэр':<25} {'И-мэйл':<30} {'Хичээл':<30}")
        print("-" * 95)
        for row in rows:
            course_name = row[3] if row[3] else "Тодорхойгүй"
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<30} {course_name:<30}")
        print("-" * 95)
        cur.close()
    except Exception as e:
        print(f"Мэдээлэл харахад алдаа гарлаа: {e}")
def main():
    conn = connect_db()
    if conn is None:
        return
    while True:
        print("\n===== Оюутан & Хичээлийн Бүртгэлийн Систем =====")
        print("1. Шинэ оюутан нэмэх")
        print("2. Оюутнуудыг хичээлтэй нь харах")
        print("3. Гарах")
        choice = input("Сонголтоо оруулна уу (1-3): ")
        if choice == '1':
            add_student(conn)
        elif choice == '2':
            view_students_with_courses(conn)
        elif choice == '3':
            print("Програмаас гарлаа.")
            break
        else:
            print("Буруу сонголт. 1-3 хооронд сонгоно уу.")
    if conn:
        conn.close()

if __name__ == "__main__":
    main()