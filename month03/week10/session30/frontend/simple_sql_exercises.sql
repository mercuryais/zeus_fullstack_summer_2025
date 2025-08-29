-- 1
select title, release_year from film order by title limit 5
-- 2
select title from film where release_year = 2006 order by title limit 5
-- 3
select  title, length from film order by length desc limit 5
-- 4
select first_name, last_name from customer order by last_name limit 5
-- 5
select c.first_name, c.last_name, co.country
from customer c
left join address a on a.address_id = c.address_id
left join city cy on a.city_id = cy.city_id 
left join country co on cy.country_id  = co.country_id
where country = 'Canada'
-- 6
select c.first_name, c.last_name, r.rental_id 
from customer c
left join rental r on c.customer_id  = r.customer_id 
-- 7
select c.first_name, c.last_name, r.rental_date
from customer c
right join rental r 
on c.customer_id = r.customer_id
-- 8
select f.title, fc.category_id
from film f
full outer join film_category fc 
on f.film_id  = fc.film_id
-- 9
select f.title
from film f
left join film_category fc on f.film_id = fc.film_id
left join category cg on cg.category_id = fc.category_id 
where name = 'Comedy'
--10
select c.first_name, c.last_name, count(r.rental_id)
from customer c
left join rental r on c.customer_id = r.customer_id
group by c.customer_id
order by count(r.rental_id)