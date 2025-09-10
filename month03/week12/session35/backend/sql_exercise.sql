-- 1
select count(film_id) as movie_count from film
-- 2
select sum(amount) from payment
-- 3
select avg(rental_rate) from film
-- 4
select min(length) as shortest_film, max(length) as longest_film
from film
-- 5
select count(distinct customer_id) from rental
-- 6
select rating, count(rating) 
from film 
group by rating
order by count desc
-- 7
select customer_id, sum(amount) as total_spent from payment
group by customer_id 
limit 5 
-- 8
select c.name, count(f.title) as number_of_films 
from category c  
left join film_category fa on c.category_id = fa.category_id
left join film f on f.film_id = fa.film_id
group by c.name
-- 9
select staff_id, count(amount) as total_transactions
from payment
group by staff_id
-- 10
select co.country, count(ci.city)
from country co
left join city ci on co.country_id = ci.country_id
group by co.country
order by count desc
-- 11
select c.customer_id, sum(p.amount) AS total_spent
FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id
order by total_spent desc