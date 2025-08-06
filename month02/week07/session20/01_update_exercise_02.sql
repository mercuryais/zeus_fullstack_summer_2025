-- Энэхүү хүснэгт нь SQL шинэчлэх үйлдлүүдийг харуулахад ашиглагдана
-- Хүснэгт үүсгэх, өгөгдөл оруулах, шинэчлэх үйлдлүүдийг агуулна
-- Хүснэгт: tasks
-- Хүснэгт нь даалгавруудын мэдээллийг хадгална
-- id, content, due, completed
CREATE TABLE IF NOT EXISTS tasks (id TEXT, content TEXT, due TEXT, completed INT);
-- Дараах датануудыг оруулна
-- 1. Start learning about SQL, 2020-06-01, 1
-- 2. Start section 2 of the course, 2020-06-08, 0
-- 3. Master SQL and PostgreSQL, 2020-06-23, 0
-- 4. Use SQL with Python, 2020-06-18, 1
INSERT INTO tasks VALUES (?, ?, ?, ?), (1, "Start learning about SQL", "2020-06-01", 1);
INSERT INTO tasks VALUES (?, ?, ?, ?), (2, "Start section 2 of the course", "2020-06-08", 0);
INSERT INTO tasks VALUES (?, ?, ?, ?), (3, "Master SQL and PostgreSQ", "2020-06-23", 0);
INSERT INTO tasks VALUES (?, ?, ?, ?), (4, "Use SQL with Python", "2020-06-18", 1);
-- Дасгал ажлууд
-- Та SQL дээр суурилсан To-Do энгийн апп дээр ажиллаж байсан.
-- Энэ апп нь даалгаврын ID, агуулга, дуусах хугацаа, мөн дууссан эсэхийг
-- хадгалдаг ганц хүснэгттэй (0 нь дуусаагүй, 1 нь дууссан гэсэн үг).
-- Та 2 ба 3-р даалгаврыг дөнгөж сая дуусгалаа. Хүснэгтийг шинэчилж үүнийг тусгана уу.
UPDATE tasks SET completed = 1 WHERE id in (2,3);