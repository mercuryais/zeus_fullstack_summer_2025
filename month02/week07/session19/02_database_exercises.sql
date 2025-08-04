-- X 1
CREATE TABLE IF NOT EXISTS students (name TEXT, major TEXT, gpa REAL);
-- X 2
INSERT INTO students (name, major, gpa) VALUES(?, ?, ?), ("Alice", "Computer Science", 3.8);
INSERT INTO students (name, major,gpa) VALUES(?, ?, ?), ("Bob", "Art", 3.2);
INSERT INTO students (name, major,gpa) VALUES(?, ?, ?), ("Charlie", "Computer Science", 3.5);
-- X 3
SELECT name, major FROM students
--X 4
SELECT * FROM students
-- X 5
SELECT * FROM students WHERE major = "Art"
-- X 6
SELECT * FROM students WHERE gpa < 3.6


CREATE TABLE IF NOT EXISTS product (product_name TEXT, product_category TEXT, price REAL);

INSERT INTO product (product_name, product_category, price) VALUES(?, ?, ?) ("Apples", "Fruit", 1.50);
INSERT INTO product (product_name, product_category, price) VALUES(?, ?, ?) ("Bread", "Bakery", 2.25);
INSERT INTO product (product_name, product_category, price) VALUES(?, ?, ?) ("Milk", "Dairy", 3.00);
INSERT INTO product (product_name, product_category, price) VALUES(?, ?, ?) ("Cheese", "Dairy", 5.50);

UPDATE product SET price = 1.75 WHERE product_name = 'Apples';
UPDATE product set price = price * 0.9 WHERE product_category = "Dairy";

INSERT INTO product (product_name, product_category, price) VALUES(?, ?, ?) ("Aaruul", "Dairy", 10,0);

DELETE FROM product WHERE product_name = "Aaruul";

DROP TABLE product;

CREATE TABLE IF NOT EXISTS icode_students (first_name TEXT, last_name TEXT, age INT, number INT)

INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Batsuuri", "Ayurzana", 20, 99698703)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Orgil", "Tumurbaatar", 20, 88120291)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Namjilsuren", "Bazarvaani", 45, 99115090)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Bolderdene", "Enhtsetseg", 21, 80230177)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Maral", "Natsagdorj", 18, 99861554)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Amirlan", "Byambasuren", 18, 90303851)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Batotgon", "Nergui", 35, 88008051)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Anhbayr", "Tsagaanbandi", 35, 99090105)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Sumyabazar", "Tsendayush", 25, 89901089)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Urantugs", "Ochirbat", 20, 00000000)
INSERT INTO icode_students VALUES(?, ?, ?, ?), ("Bulgan", "Bayasgalan", 30, 99069851)

UPDATE icode_students SET number = 99119911 WHERE first_name = "Batsuuri";
UPDATE icode_students SET number = 88118811 WHERE first_name = "Orgil";

UPDATE icode_students SET age = 16 WHERE first_name = "Maral";
UPDATE icode_students SET age = 18 WHERE first_name = "Amirlan";

DROP TABLE icode_students;