import psycopg2
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="dvdrental",
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
