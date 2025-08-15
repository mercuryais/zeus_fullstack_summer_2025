import sqlite3

CREATE_CONNECTION_SQL = """CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    game TEXT,
    score INTEGER
    )"""
INSERT_SCORES_SQL = """INSERT INTO players (name, game, score) 
    VALUES (?, ?, ?)"""
SELECT_SCORES_SQL = """SELECT * FROM players"""


def create_db():
    with sqlite3.connect("naadam.db") as conn:
        conn.execute(CREATE_CONNECTION_SQL)
        return conn
def add_score(conn, name, game, score):
    with conn:
        conn.execute(INSERT_SCORES_SQL, (name, game, score))
    print(f"✅ {name} - {game} тоглоомд {score} оноо хадгалагдлаа!")
def view_scores(conn):
    cursor = conn.cursor()
    cursor.execute(SELECT_SCORES_SQL)
    results = cursor.fetchall()
    conn.close()
    if results:
        print("\n🏆 Наадам Тэмцээний Үр Дүн:")
        for row in results:
            print(f"{row[0]}. {row[1]} | Тоглоом: {row[2]} | Оноо: {row[3]}")
    else:
        print("\nОдоогоор үр дүн байхгүй байна.")

def main():
    while True:
        conn = create_db()
        print("\nНаадам Тэмцээн")
        print("1. Шинэ тоглогч оноо нэмэх")
        print("2. Үр дүн харах")
        print("3. Гарах")
        choice = input("Сонголтоо оруулна уу: ")
        if choice == "1":
            name = input("Тоглогчийн нэр: ")
            print("Тоглоом сонгоно уу: 1. Wrestling 2. Archery 3. Horse Racing")
            game_choice = input("Тоглоомын дугаар: ")
            game_map = {"1": "Wrestling", "2": "Archery", "3": "Horse Racing"}
            game = game_map.get(game_choice, "Wrestling")
            score = int(input("Оноо: "))
            add_score(conn, name, game, score)
        elif choice == "2":
            view_scores(conn)
        elif choice == "3":
            print("👋 Баяртай!")
            break
        else:
            print("❌ Буруу сонголт!")
if __name__ == "__main__":
    main()