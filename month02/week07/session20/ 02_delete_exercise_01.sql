-- Энэхүү хүснэгт нь SQL устгах үйлдлүүдийг харуулахад ашиглагдана
-- Хүснэгт үүсгэх, өгөгдөл оруулах, устгах үйлдлүүдийг агуулна
-- Хүснэгт: vendors
-- Хүснэгт нь нийлүүлэгчдийн мэдээллийг хадгална: id, name, next_delivery
-- Дараах датануудыг оруулна
CREATE TABLE IF NOT EXISTS vendors (id TEXT, name TEXT, next_delivery TEXT);
-- 1. Strategical.ly, pending
-- 2. Techvology, done
-- 3. Deliver.academy, done
-- 4. Software house, pending
-- 5. ideasservice, done
INSERT INTO vendors (id, name, next_delivery) VALUES(?, ?, ?), (1, "Strategical.ly", "pending");
INSERT INTO vendors (id, name, next_delivery) VALUES(?, ?, ?), (2, "Techvology", "done");
INSERT INTO vendors (id, name, next_delivery) VALUES(?, ?, ?), (3, "Deliver.academy", "done");
INSERT INTO vendors (id, name, next_delivery) VALUES(?, ?, ?), (4, "Software house", "pending");
INSERT INTO vendors (id, name, next_delivery) VALUES(?, ?, ?), (5, "ideasservice", "done");
-- Дасгал ажлууд
-- Танай компани хэд хэдэн програм хангамжийн нийлүүлэгчдийг ашиглахаа больсон тул тэднийг нийлүүлэгчдийн хүснэгтээс устгахыг танаас хүсэж байна.
-- Гэсэн хэдий ч зарим нь хараахан хийгдээгүй хүргэлттэй байна.
-- Танай компанийн хамтран ажиллахаа больсон нийлүүлэгчид:
-- Strategical.ly
-- Deliver.academy
-- Нийлүүлэгчдийн хүснэгт иймэрхүү харагдаж байна:

-- | id  | name            | next_delivery |
-- | --- | --------------- | ------------- |
-- | 1   | Strategical.ly  | pending       |
-- | 2   | Techvology      | done          |
-- | 3   | Deliver.academy | done          |
-- | 4   | Software house  | pending       |
-- | 5   | ideasservice    | done          |

-- Танай компанийн хамтран ажиллахаа больсон нийлүүлэгчдээс хүлээгдэж буй хүргэлтгүйг нь устгана уу.
DELETE FROM vendors WHERE (name = "Strategical.ly" OR name = "Deliver.academy") AND next_delivery != "pending";
