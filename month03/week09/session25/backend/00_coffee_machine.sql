CREATE DATABASE coffee_machine;

CREATE TABLE resources (
    id SERIAL PRIMARY KEY,
    water INT NOT NULL,
    milk INT NOT NULL,
    coffee INT NOT NULL,
    money NUMERIC(6, 2) NOT NULL
)

INSERT INTO resources (water, milk, coffee, money)
VALUES(300, 200, 100, 0.00)

CREATE TABLE menu(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE NOT NULL,
    water INT NOT NULL,
    milk INT,
    coffee INT NOT NULL,
    cost NUMERIC(4, 2) NOT NULL
)

INSERT INTO menu (name, water, milk, coffee, cost) VALUES
('espresso', 50, 0, 18, 1.50),
('latte', 200, 150, 24, 2.50),
('cappuccino', 250, 100, 24, 3.00);