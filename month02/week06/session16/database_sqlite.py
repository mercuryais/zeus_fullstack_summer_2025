import sqlite3

connection = sqlite3.connect('diary.db')

def create_table():
    with connection:
        connection.execute("CREATE table IF NOT EXISTS entries (content TEXT, date TEXT);")
def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            'INSERT INTO entries (content, date) VALUES(?, ?);',
            (entry_content, entry_date)
        );

def get_entries():
    with connection:
        cursor = connection.execute("SELECT content, date FROM entries;")
        entries = [{"content":row[0], "date": row[1]} for row in cursor.fetchall()]
    return entries