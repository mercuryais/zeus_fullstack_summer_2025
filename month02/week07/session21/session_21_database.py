import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Creating connection with SQLite file database."""
    try:
        connection = sqlite3.connect(db_file)
        print(f"{db_file} database connected")
        return connection
    except Error as e: 
        print(e)
    return connection
def create_table(conn):
        # =============================================
        # SQL Constraints
        create_contacts_table_sql = """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """
        with conn:
              conn.execute(create_contacts_table_sql)
        # =========================================== 
        cursor = conn.cursor()
        cursor.execute("CREATE table IF NOT EXISTS contacts (id TEXT, name TEXT, email TEXT);")
        conn.commit()
def add_contact(conn, add_name, add_email):
        # =============================================
        add_contact_sql = """
            INSERT INTO contacts (name, email)
            VALUES (?, ?)
        """
        with conn:
              conn.execute(add_contact_sql, (add_name, add_email))
        #  ==========================================
        # cursor = conn.cursor()
        # cursor.execute(
        #     'INSERT INTO contacts (id, name, email) VALUES(?, ?, ?);',
        #     (id, name, email)
        # );
        # conn.commit()
def view_contacts(conn):
        # =============================================
        view_contacts = """
            SELECT * from contacts
        """
        with conn:
              cursor = conn.execute(view_contacts)
              entries = [{"ID":row[0], "Nnme": row[1], "email": row[2]} for row in cursor.fetchall()]
              print(entries)
        # =============================================
        # cursor = conn.cursor()
        # cursor.execute("SELECT * FROM contacts;")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        # conn.commit()
def update_contact_email(conn, contact_name, new_email):
        update_contact_by_name = """
            UPDATE contacts
            SET email = ? 
            WHERE name  = ?
        """
        with conn:
            conn.execute(update_contact_by_name, (new_email, contact_name))
        # =============================================
        # update_email = """
        # UPDATE contacts SET email = new_email WHERE name = name
        #     """
        # with conn:
        #       conn.execute(update_email, (name, new_email))
        # =============================================
        # cursor = conn.cursor()
        # cursor.execute(f"UPDATE contacts SET email = '{new_email}' WHERE name = '{name}';")
        # conn.commit()
def delete_contact(conn, name):
        delete_contact_sql = """
            DELETE FROM contacts WHERE name = ?
        """
        with conn:
              conn.execute(delete_contact_sql, (name,))
        # cursor = conn.cursor()
        # cursor.execute(f"DELETE FROM contacts WHERE name = '{name}';")
        # conn.commit()
def main():
    """Main function to run database operations"""
    database = "contacts.db"

    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
 
        print("\n>>> Adding initial contacts...")
        add_contact(conn, "Alice", "alice1@example.com")
        add_contact(conn, "Bob", "bob2@example.com")
        add_contact(conn,"Charlie", "charlie3@example.com")
 
 
        print(">>> Updating Bob's email...")
        update_contact_email(conn, "Bob", "bob_ne4@example.com")
 
        view_contacts(conn)
 
        print(">>> Deleting Charlie...")
        delete_contact(conn, "Charlie")
 
 
        conn.close()
        print("\nDatabase connection closed.")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()