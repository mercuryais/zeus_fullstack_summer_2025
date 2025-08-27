create table departments (
	department_id INT PRIMARY KEY,
	department_name VARCHAR(50)
);
CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	department_id INT,
	FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
-- Төслийн мэдээллийг хадгалах хүснэгт
CREATE TABLE projects (
	project_id INT PRIMARY KEY,
	project_name VARCHAR(100),
	lead_employee_id INT,
	FOREIGN KEY (lead_employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees (employee_id, first_name, last_name, department_id)
VALUES
(1, 'Alice', 'Smith', 1),
(2, 'Bob', 'Johnson', 2),
(3, 'Charlie', 'Brown', 1),
(4, 'Diana', 'Prince', 3),
(5, 'Ethan', 'Hunt', NULL), -- Ethan ямар ч хэлтэст харьяалагддаггүй
(6, 'Fiona', 'Glenanne', 2);
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Human Resources'),
(4, 'Sales'); -- Sales

-- projects хүснэгтэд өгөгдөл оруулах
INSERT INTO projects (project_id, project_name, lead_employee_id) VALUES
(101, 'Website Redesign', 2),
(102, 'Mobile App Launch', 1),
(103, 'Security Audit', 6),
(104, 'New Office Setup', NULL);

-- INNER JOIN 1
select e.first_name, e.last_name, d.department_name 
from employees e
inner join departments d  on e.department_id = d.department_id

-- INNER JOIN 2
select p.project_name, e.first_name, e.last_name
from employees e
inner join projects p on e.employee_id = p.lead_employee_id

-- LEFT JOIN 1
select e.first_name, e.last_name, d.department_name
from employees e
left join departments d on e.department_id = d.department_id

-- LEFT JOIN 2
select p.project_name, e.first_name
from projects p
left join employees e on e.employee_id = p.lead_employee_id

-- RIGHT JOIN 1
select d.department_name, e.first_name, e.last_name
from employees e
right join departments d on e.department_id = d.department_id

-- RIGHT JOIN 2
select e.first_name, e.last_name, p.project_name
from projects p 
right join employees e on e.employee_id = p.lead_employee_id

-- FULL OUTER JOIN 1
select e.first_name, e.last_name, d.department_name
from employees e
full join departments d on e.department_id = d.department_id

-- FULL OUTER JOIN 2
select p.project_name, 