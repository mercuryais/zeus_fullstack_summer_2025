import psycopg2
import os


def get_db_connection():
    """Мэдээллийн сантай холболт үүсгэж, буцаана."""
    try:
        conn = psycopg2.connect(
            dbname="dvd_rental",
            user="postgres", 
            password="",
            host="localhost", 
            port="5433" 
        )
        print("Мэдээллийн сантай амжилттай холбогдлоо.")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Холболтын алдаа: {e}")
        return None


def clear_screen():
    """Коммандын мөрийг цэвэрлэх функц."""
    os.system("cls" if os.name == "nt" else "clear")


def view_actors(conn):
    """
    Бүх жүжигчдийг тоглосон киноны тоотой нь хамт харуулна.
    (SELECT, JOIN, COUNT, GROUP BY ашиглана)
    """
    with conn.cursor() as cur:
        query = """
            select a.actor_id, a.first_name, a.last_name, count(fa.film_id)
            from actor a
            left join film_actor fa on a.actor_id = fa.actor_id
            group by a.actor_id
            order by a.actor_id 
        """
        cur.execute(query)
        actors = cur.fetchall()

        print("\n--- Жүжигчдийн Жагсаалт ---")
        print(f"{'ID':<5} | {'Нэр':<15} | {'Овог':<15} | {'Киноны тоо'}")
        print("-" * 55)
        for actor in actors:
            print(f"{actor[0]:<5} | {actor[1]:<15} | {actor[2]:<15} | {actor[3]}")
    input("\nБуцахын тулд Enter дарна уу...")


def add_actor(conn):
    first_name = input("Жүжигчний нэр: ").strip().upper()
    last_name = input("Жүжигчний овог: ").strip().upper()

    if not first_name or not last_name:
        print("Нэр, овог хоосон байж болохгүй.")
        return

    with conn.cursor() as cur:
        try:
            cur.execute(
                """
                insert into actor (first_name, last_name)
                values (%s, %s)
            """, (first_name, last_name)
            )
            conn.commit()
            print(f"'{first_name} {last_name}' нэртэй жүжигчнийг амжилттай нэмлээ.")
        except Exception as e:
            conn.rollback()
            print(f"Алдаа гарлаа: {e}")
    input("\nБуцахын тулд Enter дарна уу...")


def update_actor(conn):
    """
    Жүжигчний мэдээллийг шинэчилнэ. (UPDATE ашиглана)
    """
    try:
        actor_id = int(input("Шинэчлэх жүжигчний ID-г оруулна уу: "))
    except ValueError:
        print("ID зөвхөн тоо байх ёстой.")
        return

    new_first_name = input(f"Шинэ нэр (хоосон бол хуучнаар үлдээнэ): ").strip().upper()
    new_last_name = input(f"Шинэ овог (хоосон бол хуучнаар үлдээнэ): ").strip().upper()

    with conn.cursor() as cur:
        cur.execute(
            """select * from actor where actor_id=%s"""
            , (actor_id,)
        )
        actor = cur.fetchone()

        if not actor:
            print(f"{actor_id} ID-тай жүжигчин олдсонгүй.")
            return

        final_first_name = new_first_name if new_first_name else actor[1]
        final_last_name = new_last_name if new_last_name else actor[2]

        try:
            cur.execute(
                """
                UPDATE actor SET first_name=%s, last_name=%s WHERE actor_id = %s
        """, (final_first_name, final_last_name, actor_id)
            )
            conn.commit()
            print(f"{actor_id} ID-тай жүжигчний мэдээллийг амжилттай шинэчиллээ.")
        except Exception as e:
            conn.rollback()
            print(f"Алдаа гарлаа: {e}")
    input("\nБуцахын тулд Enter дарна уу...")


def delete_actor(conn):
    """
    Жүжигчнийг устгана. (DELETE ашиглана)
    """
    try:
        actor_id = int(input("Устгах жүжигчний ID-г оруулна уу: "))
    except ValueError:
        print("ID зөвхөн тоо байх ёстой.")
        return

    confirm = input(
        f"{actor_id} ID-тай жүжигчнийг устгахдаа итгэлтэй байна уу? (yes/no): "
    ).lower()
    if confirm != "yes":
        print("Устгах үйлдэл цуцлагдлаа.")
        return

    with conn.cursor() as cur:
        try:
            cur.execute(
                """delete from actor where actor_id=%s""", (actor_id,)
            )
            if cur.rowcount > 0:
                print(f"{actor_id} ID-тай жүжигчнийг амжилттай устгалаа.")
            else:
                print(f"{actor_id} ID-тай жүжигчин олдсонгүй.")
        except psycopg2.errors.ForeignKeyViolation:
            conn.rollback()
            print(f"АЛДАА: Энэ жүжигчин кинонд тоглосон тул устгах боломжгүй.")
        except Exception as e:
            conn.rollback()
            print(f"Алдаа гарлаа: {e}")
    input("\nБуцахын тулд Enter дарна уу...")


def show_stats(conn):
    with conn.cursor() as cur:
        cur.execute(
            """select count(actor_id) from actor"""
        )
        count = cur.fetchone()[0]
        print(f"\nНийт жүжигчдийн тоо: {count}")
    input("\nБуцахын тулд Enter дарна уу...")


def main():
    """Програмын үндсэн цэс болон удирдах хэсэг."""
    conn = get_db_connection()
    if not conn:
        return

    while True:
        clear_screen()
        print("\n===== Жүжигчин Удирдах Програм =====")
        print("1. Жүжигчдийн жагсаалтыг харах")
        print("2. Шинэ жүжигчин нэмэх")
        print("3. Жүжигчний мэдээлэл шинэчлэх")
        print("4. Жүжигчин устгах")
        print("5. Статистик харах")
        print("6. Гарах")

        choice = input("Сонголтоо оруулна уу: ")

        if choice == "1":
            view_actors(conn)
        elif choice == "2":
            add_actor(conn)
        elif choice == "3":
            update_actor(conn)
        elif choice == "4":
            delete_actor(conn)
        elif choice == "5":
            show_stats(conn)
        elif choice == "6":
            break
        else:
            print("Буруу сонголт. 1-6 хооронд тоо оруулна уу.")
            input("\nБуцахын тулд Enter дарна уу...")

    conn.close()
    print("Програмаас гарлаа.")


if __name__ == "__main__":
    main()
