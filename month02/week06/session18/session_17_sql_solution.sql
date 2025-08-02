--  X 1.1
CREATE TABLE IF NOT EXISTS booklist (name TEXT, author TEXT, date TEXT);

-- X 1.2
CREATE TABLE IF NOT EXISTS criticizer (name TEXT, location TEXT, count INT);

-- X 1.3
CREATE TABLE IF NOT EXISTS termometer (temperature REAL, date TEXT, time TEXT);


-- X 2.1

CREATE TABLE IF NOT EXISTS (id TEXT, first_name TEXT, surname TEXT, salary INT); 

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (1, "Rolf", "Smith", 55000);

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (2, "Bob", "Smith", 45000);

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (3, "Anne", "Pun", 87000);
