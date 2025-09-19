import psycopg2
import os

class DatabaseManager:
    def __init__(self):
        self.conn_params = {
            "dbname" : "dvd_rental",
            "user" : "postgres", 
            "password" : "",
            "host" : "localhost", 
            "port" :  "5433" 
        }
        self.conn = None

    def connect(self):
        """Мэдээллийн сантай холбогдоно."""
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            print("Мэдээллийн сантай амжилттай холбогдлоо.")
        except psycopg2.OperationalError as e:
            print(f"Холболтын алдаа: {e}")
            self.conn = None

    def disconnect(self):
        """Холболтыг салгана."""
        if self.conn:
            self.conn.close()
            print("Холболтыг салголоо.")

    def execute_query(self, query, params=None, fetch=None):
        """Асуулга ажиллуулж, үр дүнг буцаана."""
        if not self.conn:
            print("Холболт байхгүй байна.")
            return None
        
        with self.conn.cursor() as cur:
            try:
                cur.execute(query, params)
                self.conn.commit()
                
                if fetch == 'one':
                    return cur.fetchone()
                if fetch == 'all':
                    return cur.fetchall()
                if cur.description is not None:
                     return cur.rowcount # UPDATE, DELETE-д зориулагдсан
                return True # INSERT-д зориулагдсан
            
            except Exception as e:
                self.conn.rollback()
                print(f"Асуулгын алдаа: {e}")
                return None

class ActorApp:
    """Хэрэглэгчийн интерфейс болон програмын логикийг удирдах үндсэн класс."""
    def __init__(self):
        self.db = DatabaseManager()

    def clear_screen(self):
        """Коммандын мөрийг цэвэрлэнэ."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def view_actors(self):
        query = """
           select * from actor order by actor_id
        """
        actors = self.db.execute_query(query, fetch='all')
        if actors is not None:
            print("\n--- Жүжигчдийн Жагсаалт ---")
            print(f"{'ID':<5} | {'Нэр':<15} | {'Овог':<15} | {'Киноны тоо'}")
            print("-" * 55)
            for actor in actors:
                print(f"{actor[0]:<5} | {actor[1]:<15} | {actor[2]:<15} | {actor[3]}")
        input("\nБуцахын тулд Enter дарна уу...")

    def add_actor(self):
        first_name = input("Жүжигчний нэр: ").strip().upper()
        last_name = input("Жүжигчний овог: ").strip().upper()
        if not first_name or not last_name:
            print("Нэр, овог хоосон байж болохгүй.")
            input("\nБуцахын тулд Enter дарна уу...")
            return
            
        query = """
            insert into actor (first_name, last_name)
            values (%s , %s)
        """
        if self.db.execute_query(query, (first_name, last_name)):
            print(f"'{first_name} {last_name}' нэртэй жүжигчнийг амжилттай нэмлээ.")
        input("\nБуцахын тулд Enter дарна уу...")
        
    def update_actor(self):
        try:
            actor_id = int(input("Шинэчлэх жүжигчний ID-г оруулна уу: "))
        except ValueError:
            print("ID зөвхөн тоо байх ёстой.")
            input("\nБуцахын тулд Enter дарна уу...")
            return

        new_first_name = input("Шинэ нэр (хоосон бол хуучнаар үлдээнэ): ").strip().upper()
        new_last_name = input("Шинэ овог (хоосон бол хуучнаар үлдээнэ): ").strip().upper()

        actor = self.db.execute_query("SELECT first_name, last_name FROM actor WHERE actor_id = %s", (actor_id,), fetch='one')
        if not actor:
            print(f"{actor_id} ID-тай жүжигчин олдсонгүй.")
            input("\nБуцахын тулд Enter дарна уу...")
            return

        final_first_name = new_first_name or actor[0]
        final_last_name = new_last_name or actor[1]

        query = """
            update actor set first_name=%s, last_name=%s where actor_id=%s
        """
        if self.db.execute_query(query, (final_first_name, final_last_name, actor_id)):
            print(f"{actor_id} ID-тай жүжигчний мэдээллийг амжилттай шинэчиллээ.")
        input("\nБуцахын тулд Enter дарна уу...")

    def delete_actor(self):
        try:
            actor_id = int(input("Устгах жүжигчний ID-г оруулна уу: "))
        except ValueError:
            print("ID зөвхөн тоо байх ёстой.")
            input("\nБуцахын тулд Enter дарна уу...")
            return
        
        confirm = input(f"{actor_id} ID-тай жүжигчнийг устгахдаа итгэлтэй байна уу? (yes/no): ").lower()
        if confirm != 'yes':
            print("Устгах үйлдэл цуцлагдлаа.")
            input("\nБуцахын тулд Enter дарна уу...")
            return

        query = """
            delete from actor where actor_id=%s
        """
        result = self.db.execute_query(query, (actor_id,))

        if result is not None:
             if result > 0:
                 print(f"{actor_id} ID-тай жүжигчнийг амжилттай устгалаа.")
             else:
                 print(f"{actor_id} ID-тай жүжигчин олдсонгүй.")
        input("\nБуцахын тулд Enter дарна уу...")
        
    def show_stats(self):
        query = """
            select count(actor_id) from actor
        """
        count = self.db.execute_query(query, fetch='one')
        if count:
            print(f"\nНийт жүжигчдийн тоо: {count[0]}")
        input("\nБуцахын тулд Enter дарна уу...")

    def run(self):
        """Програмын үндсэн гогцоог ажиллуулна."""
        self.db.connect()
        if not self.db.conn:
            return

        while True:
            self.clear_screen()
            print("\n===== Жүжигчин Удирдах Програм (OOP хувилбар) =====")
            print("1. Жүжигчдийн жагсаалтыг харах")
            print("2. Шинэ жүжигчин нэмэх")
            print("3. Жүжигчний мэдээлэл шинэчлэх")
            print("4. Жүжигчин устгах")
            print("5. Статистик харах")
            print("6. Гарах")
            
            choice = input("Сонголтоо оруулна уу: ")

            actions = {
                '1': self.view_actors,
                '2': self.add_actor,
                '3': self.update_actor,
                '4': self.delete_actor,
                '5': self.show_stats,
            }

            action = actions.get(choice)
            if action:
                action()
            elif choice == '6':
                break
            else:
                print("Буруу сонголт. 1-6 хооронд тоо оруулна уу.")
                input("\nБуцахын тулд Enter дарна уу...")

        self.db.disconnect()

if __name__ == "__main__":
    app = ActorApp()
    app.run()