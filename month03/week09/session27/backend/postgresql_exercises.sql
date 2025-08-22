select * from payment limit 10;

select * from payment
where amount between 3.00 and 5.00
order by amount asc;

select title, length from film
where length between 90 and 120
order by length desc;

select rental_id, rental_date from rental 
where rental_date between '2005-05-25 00:00:00' 
and '2005-05-26 23:59:59'

select title, replacement_cost from film 
where replacement_cost between 15.00 and 20.00;

select * from customer 
where customer_id between 100 and 200


select title from film where title = 'Italian';

select title from film where title like 'Italian';

-- EX 1
select * from actor where last_name like 'D%';

-- EX 2
select * from film where title like '%action%';

-- EX 3
select * from customer where first_name like '%er';

-- EX 4
select * from film where title like '_e%';

-- EX 5
select * from actor where last_name like '%gen%';

select r.rental_id, c.customer_id, c.first_name, c.last_name 
from rental r
join customer c
on r.customer_id = c.customer_id

-- EX 1

select address, district, address 2 
from address
where address2 is null;

-- EX 2
select rental_id, customer_id, return_date
from rental 
where return_date is not nullcustomer_idlimit 10

--EX 3
select c.first_name, c.last_name, a.address, a.address2
from customer c
join address a 
on c.address_id = a.address_id
where a.address2 is not null


--EX 4
select first_name, last_name from staff 
where picture is null

