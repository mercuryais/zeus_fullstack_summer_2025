select count(*) from film;

select sum(amount) from payment

select AVG(rental_rate) from film

select min(length), max(length) from film

select count(distinct customer_id) from rental

select rating, count(*) as number_of_films
from film
group by rating

select customer_id, sum(amount) from payment group by customer_id
order by customer_id asc

select c.name, count(*) as number_of_films
from category c 
left join film_category fc on c.category_id = fc.category_id
left join film f on f.film_id = fc.film_id
group by c."name" 

select s.staff_id, count(p.amount)
from staff s 
left join payment p on s.staff_id = p.staff_id
group by s.staff_id

select c.country, count(cy.city)
from country c
left join city cy on c.country_id = cy.country_id
group by c.country

select c.customer_id, sum(p.amount)
from customer c
left join payment p on c.customer_id = p.customer_id
group by c.customer_id

select c.name, avg(f.rental_duration )
from category c
left join film_category fc on c.category_id = fc.category_id
left join film f on fc.film_id = f.film_id
group by c.name

select a.first_name, a.last_name, count(f.film_id)
from actor a 
left join film_actor fa on a.actor_id = fa.actor_id
left join film f on f.film_id = fa.film_id
group by a.first_name, a.last_name