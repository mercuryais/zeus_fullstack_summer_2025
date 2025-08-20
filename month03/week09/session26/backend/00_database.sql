CREATE TABLE Authors (
    id INT primary key,
    author_name TEXT,
    country VARCHAR(50)
)
CREATE TABLE Books (
	id SERIAL primary key,
	title TEXT not null,
	publication_year integer not null,
	author_id INTEGER,
	foreign key (author_id) references authors(id) on delete cascade 
);

INSERT INTO Authors (author_name, country) VALUES
('Ж.К. Роулинг', 'Их Британи'),
('Жорж Орвелл', 'Их Британи'),
('Харүки Мүраками', 'Япон');


INSERT INTO Books (title, publication_year, author_id) VALUES
('Харри Поттэр', 1997, 1),
('1984', 1949, 2),
('Амьтны ферм', 1945, 2),
('Норвегийн ой', 1987, 3);

SELECT title, publication year FROM Books;

SELECT author_name FROM Authors Where country = "Их Британи";

SELECT title FROM Books WHERE publication_year IN (1945, 1997);

SELECT author_name FROM Authors WHERE country IN ("Их Британи", "Япон");

SELECT Books.title, Authors.author_name
FROM Books
JOIN Authors ON Books.author_id = Authors.author_id;
WHERE Authors.author_name = "Жорж Орвелл";

UPDATE Books SET publication_year=1998 WHERE title = "Харри Поттер";

UPDATE Authors SET country="АНУ" WHERE author_name = "Харүки Мүраками";

DELETE FROM Books WHERE title="Амьтны ферм";

DELETE FROM Authors WHERE country = "Их Британи";

INSERT INTO Authors(author_id, author_name, country)
VALUES (4, "Стивен Кинг", "АНУ");

INSERT INTO Books(book_id, title, publication_year, author_id)
VALUES (105, "Дэлхийн дайн", 2023, 4)