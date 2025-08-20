import psycopg2
import os
DB_NAME = "Books"
DB_USER = "postgres"
DB_PASS = ""
DB_HOST = "localhost"
DB_PORT = "5433"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def list_authors():
    conn = None
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("select * from Authors")
        authors = cursor.fetchall()
        print("\n--- 📚 Бүх Зохиогчид ---")
        for author in authors:
            print(f" ID: {author[0]}, Нэр: {author[1]}, Улс: {author[2]}")
        print("------------------------\n")
    except psycopg2.Error as e:
        print(f"Database алдаа: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
def list_books_by_author():
    conn = None
    try:
        author_id = input("Номуудыг нь харахыг хүссэн зохиогчийн ID-горуулна уу: ")
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        query = """
        SELECT b.title, b.publication_year, a.author_name
        FROM Books b
        JOIN Authors a ON b.author_id = a.author_id
        WHERE b.author_id = %s;
        """
        cursor.execute(query, (int(author_id),))
        books = cursor.fetchall()
        if books:
            author_name = books[0][2]
            print(f"\n--- ✍'{author_name}' зохиогчийн номууд ---")
            for book in books:
                print(f" Гарчиг: {book[0]}, Хэвлэгдсэн он: {book[1]}")
            print("-------------------------------------------\n")
        else:
            print(f"{author_id} ID-тай зохиогч олдсонгүй эсвэл ном байхгүй байна.")
    except (psycopg2.Error, ValueError) as e:
        print(f"Алдаа: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

def add_book():
    conn = None
    try:
        author_id = input("Ном нэмэх зохиогчийн ID-г оруулна уу: ")
        title = input("Номын гарчгийг оруулна уу: ")
        year = input("Хэвлэгдсэн оныг оруулна уу: ")
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        query = """
        INSERT INTO Books(title, publication_year, author_id)
        VALUES(%s, %s, %s)
        """
        cursor = conn.cursor()
        cursor.execute(query, (title, int(year), int(author_id)))
        conn.commit()
        print(f"\n✅ '{title}' номыг амжилттай нэмлээ!\n")
    except (psycopg2.Error, ValueError) as e:
        print(f"\n❌ Алдаа гарлаа: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()

def main():
    while True:
        print("--- Номын Сангийн Менежер ---")
        print("1. Бүх зохиогчийг харах")
        print("2. Зохиогчийн номуудыг харах")
        print("3. Шинэ ном нэмэх")
        print("4. Гарах")
        choice = input("Та сонголтоо хийнэ үү (1-4): ")
        clear_screen()
        if choice == '1':
            list_authors()
        elif choice == '2':
            list_books_by_author()
        elif choice == '3':
            add_book()
        elif choice == '4':
            print("Баяртай!")
            break
        else:
            print("Буруу сонголт. 1-4 хооронд сонгоно уу.")
        input("\nҮргэлжлүүлэхийн тулд Enter дарна уу...")
        clear_screen()
if __name__ == "__main__":
    main()