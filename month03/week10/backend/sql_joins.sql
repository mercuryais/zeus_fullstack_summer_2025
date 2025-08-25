-- JOINS

-- LEFT
-- RIGHT
-- INNER
-- OUTERselect * from country;

select * from city;

select * from city where country_id = 86;

select * from city ci join country co on ci.country_id = co.country_id;

select city_id, city, country  from city ci join country co on ci.country_id = co.country_id;

select a.first_name, a.last_name, COUNT(fa.film_id) as number_of_films
from actor a
left join film_actor fa on a.actor_id  = fa.actor_id
group by a.actor_id
order by number_of_films asc;

select c.first_name, c.last_name, p.payment_id, p.amount 
from payment p
left join customer c  on c.customer_id = p.customer_id
where p.payment_id  is null
order by p.amount asc

-- RIGHT JOIN

select r.rental_date, c.first_name, c.last_name
from rental r
right join customer c on r.customer_id = c.customer_id
order by r.rental_date desc;

select f.title, i.inventory_id, i.store_id
from film f
right join inventory i on f.film_id  = i.film_id

select a.first_name, fa. film_id 
from film_actor fa 
right join actor a on a.actor_id  = fa.actor_id
order by fa.film_id

-- inner join

select c.first_name, c.last_name, a.district
from customer c
inner join address a  on c.address_id = a.address_id

select f.title, c.name as category_name
from film f
inner join film_category fc on f.film_id = fc.film_id
inner join category c on fc.category_id  = c.category_id;

--exercise 3
select r.rental_id, s.first_name, s.last_name
from rental r
inner join staff s on r.staff_id = s.staff_id

--FULL OUTER JOIN
select c.first_name , c.last_name, s/first_name, s.last_name
from customer c
full outer join staff s
on c.first_name = s.first_name and c.last_name  = s.last_name
