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
    pass