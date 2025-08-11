import sqlite3
import datetime

# Movie table id нь primary key, автоматаар өсдөг
# title text type, release_timestamp real, watched integer
CREATE_MOVIES_TABLE_SQL = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIES_SQL = """INSERT INTO movies (title, release_timestamp, watched)
VALUES (?, ?, 0);"""
# SELECT_ALL_MOVIES_SQL = бүх movies утгыг харуулах query бичнэ.
SELECT_ALL_MOVIES_SQL = """SELECT * FROM movies;"""
# SELECT_UPCOMING_MOVIES_SQL = release_timestamp-аас их бүх утгыг харуулах query бичнэ.
SELECT_UPCOMING_MOVIES_SQL = """SELECT * FROM movies WHERE release_timestamp > ?;"""
# SELECT_WATCHED_MOVIES_SQL = бүх watched нь 1 байгаа утгуудыг харуулах query бичнэ.
SELECT_WATCHED_MOVIES_SQL = """SELECT * FROM movies WHERE watched = 1;"""
# SET_MOVIE_WATCHED_SQL = movie-гийн title-д нь тохирсон утгын watched-ийг 1 болгоно.
SET_MOVIE_WATCHED_SQL = """UPDATE movies SET watched = 1 WHERE title = ?;"""

connection = sqlite3.connect('movies.db')

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE_SQL)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES_SQL, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES_SQL, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES_SQL)
        return cursor.fetchall()


def watch_movie(title):
    with connection:
        connection.execute(SET_MOVIE_WATCHED_SQL, (title,))

def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES_SQL)
        return cursor.fetchall()