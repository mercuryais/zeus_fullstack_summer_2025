create table courses (
	id serial primary key,
	course_name varchar(50) unique not null
)
insert into courses (course_name) values
('Програмчлалын үндэс'),
('Өгөгдлийн сангийн зохиомж'),
('Веб хөгжүүлэлт')

drop table students;

create table students (
	id serial primary key,
	ovog_ner varchar(100) not null,
	email varchar(100) unique,
	utas varchar(20),
	course_id integer,
	foreign key (course_id) references courses(id)
)
select s.id, s.ovog_ner, s.email, c.course_name
from students s
left join courses c on s.course_id = c.id