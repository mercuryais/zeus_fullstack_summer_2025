CREATE TABLE IF NOT EXISTS users (id TEXT, first_name TEXT, surname TEXT, salary INT)

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (1, "Rolf", "Smith", 55000);

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (2, "Bob", "Smith", 45000);

INSERT INTO users (id, first_name , surname, salary) VALUES(?, ?, ?, ?), (3, "Anne", "Pun", 87000);

SELECT * FROM users WHERE salary >= 60000

SELECT surname FROM users WHERE salary >= 80000 OR age >= 50

SELECT * FROM users WHERE salary >= 35000 AND age <=20 or salary >= 80000 and age <=30