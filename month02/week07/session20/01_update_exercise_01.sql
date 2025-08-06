-- Энэхүү хүснэгт нь SQL шинэчлэх үйлдлүүдийг харуулахад ашиглагдана
-- Хүснэгт үүсгэх, өгөгдөл оруулах, шинэчлэх үйлдлүүдийг агуулна
-- Хүснэгт: employees
CREATE TABLE IF NOT EXISTS employees (id TEXT, first_name TEXT, surname TEXT, salary INT)
-- Хүснэгт нь ажилтнуудын мэдээллийг хадгална: id, first_name, surname, salary
-- Дараах датануудыг оруулна
-- 1. Rolf Smith, 55000
-- 2. Bob Smith, 45000
-- 3. Anne Pun, 87000
-- 4. Charlie Robert, 33000
-- 5. Mary Lee, 31000
-- 6. Adam Roo, 47000
INSERT INTO employees (id, first_name, surname, salary) VALUES(?, ?, ?, ?), (1, "Rolf", "Smith", 55000)
INSERT INTO employees (id, first_name, surname, salary) VALUES(?, ?, ?, ?), (2, "Bob", "Smith", 45000)
INSERT INTO employees (id, first_name, surname, salary) VALUES(?, ?, ?, ?), (3, "Anne", "Pun", 87000)
INSERT INTO employees (id, first_name, surname, salary) VALUES(?, ?, ?, ?), (4, "Charlie", "Robert", 33000)
INSERT INTO employees (id, first_name, surname, salary) VALUES(?, ?, ?, ?), (5, "Mary", "Lee", 31000)
INSERT INTO employees (id, first_name, surname, salary) VALUES(?, ?, ?, ?), (6, "Adam", "Roo", 47000)
-- Дасгал ажлууд
-- Таны ажилладаг компани ажилчдын цалингийн доод хэмжээг тогтоосон.
-- Ямар ч ажилтан 35000-аас бага цалин авч болохгүй.
-- Өгөгдсөн хүснэгтийн датаг ямар ч ажилтан 35000-аас бага цалин
-- авахгүй байхаар шинэчилнэ үү.
UPDATE employees SET salary = 35000 WHERE salary < 35000