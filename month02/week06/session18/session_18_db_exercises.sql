CREATE TABLE IF NOT EXISTS users (id int, first_name TEXT, surname TEXT, salary INT, age INT);

INSERT INTO users (id, first_name , surname, salary, age) VALUES(?, ?, ?, ?, ?), (1, "Rolf", "Smith", 55000, 57);
	
INSERT INTO users (id, first_name , surname, salary, age) VALUES(?, ?, ?, ?, ?), (2, "Bob", "Smith", 45000, 18);

INSERT INTO users (id, first_name , surname, salary, age) VALUES(?, ?, ?, ?, ?), (3, "Anne", "Pun", 87000, 49);

INSERT INTO users (id, first_name , surname, salary, age) VALUES(?, ?, ?, ?, ?), (4, "Elisabeth", "Lee", 90000, 29);

SELECT * FROM users WHERE salary >= 60000

SELECT surname FROM users WHERE salary >= 80000 OR age >= 50

SELECT * FROM users WHERE salary >= 35000 AND age <=20 or salary >= 80000 and age <=30

