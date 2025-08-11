import sqlite3

def connect_db(): 
    connection = sqlite3.connect('tasks.db')
    print("tasks.db database connected")
    return connection
def create_table(connection):
    create_tasks_table_sql = """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT NOT NULL
        );
    """
    with connection:
            connection.execute(create_tasks_table_sql)
def add_task(connection, description, priority):
    status = "pending"
    add_task_sql = """
        INSERT INTO tasks (description, priority, status)
        VALUES (?, ?, ?)
    """
    with connection:
        connection.execute(add_task_sql, (description, priority, status))
def view_tasks(connection):
    #     view_contacts = """
    #     SELECT * from contacts
    # """
    # with connection:
    #     cursor = conn.execute(view_contacts)
    #     entries = [{"ID":row[0], "Nnme": row[1], "email": row[2]} for row in cursor.fetchall()]
    pass
def update_task_status(connection, task_id):
        update_status_by_name = """
        UPDATE tasks
        SET status = Complete
        WHERE id  = ?
    """
        with connection:
            connection.execute(update_status_by_name, (task_id))
def delete_task(connection, task_id):
        delete_task_sql = """
            DELETE FROM tasks WHERE id = ?
        """
        with connection:
              connection.execute(delete_task_sql, (task_id,))
def main():
    connection = connect_db()
    create_table(connection)
    while True:
        print("\nTODO жагсаалт:")
        print("1. Үүрэг нэмэх")
        print("2. Бүх үүргүүдийг харах")
        print("3. Үүрэг дуусгавар болгох")
        print("4. Үүрэг устгах")
        print("5. Гарах")
        choice = input("Та сонголтоо оруулна уу (1-5): ")
        if choice == '1':
            description = input("Үүргийн тодорхойлолт оруулна уу: ")
            priority = input("Чухал эсэх (High, Medium, Low): ")
            add_task(connection, description, priority)
        elif choice == '2':
            view_tasks(connection)
        elif choice == '3':
            task_id = int(input("Дуусгах үүргийн ID оруулна уу: "))
            update_task_status(connection)
        elif choice == '4':
            task_id = int(input("Устгах үүргийн ID оруулна уу: "))
            delete_task(connection, task_id)
        elif choice == '5':
            print("Програмыг хааж байна...")
            break
        else:
            print("Буруу сонголт! Дахин оролдоно уу.")
if __name__ == "__main__":
    main()