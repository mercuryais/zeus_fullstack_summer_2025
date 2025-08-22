CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, date TEXT);

CREATE TABLE IF NOT EXISTS book_reviewers (name TEXT, location TEXT, count INT);

CREATE TABLE IF NOT EXISTS temperature_readings (temperature REAL, date TEXT, time TEXT);

CREATE TABLE IF NOT EXISTS users (id TEXT, first_name TEXT, surname TEXT, salary INT)

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (1, "Rolf", "Smith", 55000);
	
INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (2, "Bob", "Smith", 45000);

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (3, "Anne", "Pun", 87000);

SELECT * FROM users;

SELECT first_name, surname FROM users;

SELECT surname, salary FROM users

-- WHERE clause
SELECT * FROM USERS; -- all users entry

SELECT * FROM users WHERE first_name = 'John';

SELECT * FROM users WHERE surname = 'Smith';

SELECT salary FROM users WHERE first_name = 'Anne'

-- = operator
SELECT * FROM users WHERE salary > 50000;

-- SQL Comparison operators
-- (<) --- Lower Than
-- (>) --- Greater Than
-- (<=) --- Greater Than or equal to
-- (=) --- Exactly equal to
-- (!=) --- Not equal to
-- (<>) --- Not equal to

-- SQL Multi Comparisons
-- AND OR comparisons

SELECT * FROM users WHERE surname = "Smith" AND salary > 50000;
SELECT * FROM users WHERE salary > 50000 OR salary < 40000;

