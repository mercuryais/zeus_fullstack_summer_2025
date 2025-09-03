import psycopg2
from psycopg2 import OperationalError
def connect_db():
    try:
        conn = psycopg2.connect(
        dbname="session_32",
        user="postgres",
        password="",
        host="localhost",
        port="5433"
        )
        return conn
    except OperationalError as e:
        print(f"Холболтын алдаа гарлаа: {e}")
        return None
def setup_database(conn):
    try:
        cur = conn.cursor()
        create_courses_sql =  """ create table if not exists courses (
            id serial primary key,
            course_name varchar(20) unique not null
    )"""
        cur.execute(create_courses_sql)
        create_students_sql = """ create table if not exists students (
        id serial primary key,
        ovog_ner varchar(40) not null,
        email varchar(40) unique not null,
        grade integer check (grade >= 0 and grade <=100),
        course_id integer,
        foreign key (course_id) references courses(id)
        )"""
        cur.execute(create_students_sql)
        cur.execute("""INSERT INTO courses (course_name)
        VALUES
        ('Програмчлалын үндэс'),
        ('Веб хөгжүүлэлт'),
        ('Өгөгдлийн сан') ON CONFLICT (course_name) DO NOTHING;
        """)
        conn.commit()
        cur.close()
        print("Мэдээллийн сангийн бүтэц амжилттай бэлтгэгдлээ.")
    except Exception as e:
        print(f"Мэдээллийн сан бэлтгэхэд алдаа гарлаа: {e}")
        conn.rollback()
def view_courses(conn):
    try:
        cur = conn.cursor()
        select_courses_sql = """
            select * from courses
        """
        cur.execute(select_courses_sql)
        courses = cur.fetchall()
        print("\n--- Боломжит хичээлүүд ---")
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
        print("Бүртгэлтэй хичээл алга байна.")
        return
    try:
        ovog_ner = input("Оюутны овог нэрийг оруулна уу: ")
        email = input("И-мэйл хаягийг оруулна уу: ")
        grade = -1
        while not (0 <= grade <= 100):
            try:
                grade = int(input("Дүнг оруулна уу (0-100): "))
            except ValueError:
                print("Зөвхөн тоон утга оруулна уу.")
        course_id_str = ""
        valid_ids = [str(c[0]) for c in courses]
        while course_id_str not in valid_ids:
            course_id_str = input("Дээрх жагсаалтаас хичээлийн ID-г сонгоно уу: ")
        cur = conn.cursor()
        query = """
            insert into students (ovog_ner, email, grade, course_id)
            values(%s, %s, %s, %s)
        """
        cur.execute(query, (ovog_ner, email, grade, int(course_id_str)))
        conn.commit()
        print(f"'{ovog_ner}' амжилттай бүртгэгдлээ.")
        cur.close()
    except Exception as e:
        print(f"Оюутан нэмэхэд алдаа гарлаа: {e}")
        conn.rollback()

def show_course_statistics(conn):
    try:
        cur = conn.cursor()
        statistic_sql = """
        select c.course_name, count(s), avg(s.grade), max(s.grade), min(s.grade)
        from courses c
        left join students s on c.id = s.course_id
        group by c.course_name 
        """
        cur.execute(statistic_sql)
        rows = cur.fetchall()
        if not rows:
            print("Статистик гаргах мэдээлэл олдсонгүй.")
            return
        print("\n--- Хичээлүүдийн Дүнгийн Нэгдсэн Тайлан ---")
        print(f"{'Хичээлийн нэр':<25} {'Оюутны тоо':<15} {'Дундаж дүн': <15} {'Их дүн':<10} {'Бага дүн':<10}")
        print("-" * 85)
        for row in rows:
            student_count = row[1]
            avg_grade = row[2] if student_count > 0 else 0
            max_grade = row[3] if student_count > 0 else 0
            min_grade = row[4] if student_count > 0 else 0
            print(f"{row[0]:<25} {student_count:<15} {avg_grade:<15.2f} {max_grade:<10} {min_grade:<10}")
            print("-" * 85)
        cur.close()
    except Exception as e:
        print(f"Статистик харахад алдаа гарлаа: {e}")

def main():
    conn = connect_db()
    if conn is None:
        return
    setup_database(conn)
    while True:
        print("\n===== Оюутны Дүнгийн Систем =====")
        print("1. Шинэ оюутан бүртгэх")
        print("2. Хичээлийн дүнгийн тайлан харах")
        print("3. Гарах")
        choice = input("Сонголтоо оруулна уу (1-3): ")
        if choice == '1':
            add_student(conn)
        elif choice == '2':
            show_course_statistics(conn)
        elif choice == '3':
            print("Програмаас гарлаа.")
            break
        else:
            print("Буруу сонголт. 1-3 хооронд сонгоно уу.")
            if conn:
                conn.close()
if __name__ == "__main__":
    main()