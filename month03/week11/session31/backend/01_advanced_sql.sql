-- EX 1
select a.first_name, a.last_name, f.title, c.name
from actor a
left join film_actor fa on a.actor_id = fa.actor_id
left join film f on fa.film_id = f.film_id
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id  = c.category_id
where a.first_name = 'Penelope' and a.last_name = 'Guiness'
-- EX 2
select c.first_name, c.last_name, c.email
from customer c
left join rental r on c.customer_id  = r.rental_id
left join inventory i on i.inventory_id  = r.inventory_id
left join film f on f.film_id = i.film_id
left join film_category fc on fc.category_id =f.film_id
left join category ca on ca.category_id = fc.category_id
where ca.name != 'Horror'
-- EX 3
select f.title, a.first_name, a1.first_name
from film f 
left join film_actor fa on f.film_id  = fa.film_id
left join film_actor fa1 on f.film_id = fa.film_id 
left join actor a on fa.actor_id = a.actor_id
left join actor a1 on fa1.actor_id = a1.actor_id
where a.actor_id < a1.actor_id
-- EX 4
select f.title, a.last_name, f.rental_duration, f.rating
from film f
left join film_actor fa on f.film_id = fa.film_id
left join actor a on fa.actor_id = a.actor_id
where f.rating = 'PG-13' and F.rental_duration = 7  and 
a.last_name like 'D%'
-- EX 5
	select c.first_name, c.last_name, c.email, c.create_date 
	from customer c 
	order by c.create_date desc limit 1
-- EX 6
select c.first_name, c.last_name, f.title, 
case
	when f.rental_duration < 4 then 'Bogino'
	when f.rental_duration >=4 and f.rental_duration < 7 then 'Dund'
	when f.rental_duration > 7 then 'Urt'
	else 'None'
end as rental_date_result
from customer c
left join rental r on c.customer_id  = r.rental_id
left join inventory i on i.inventory_id  = r.inventory_id
left join film f on f.film_id = i.film_id
-- EX 7
select distinct c.email 
from customer c
left join rental r on c.customer_id  = r.rental_id
left join inventory i on i.inventory_id  = r.inventory_id
left join film f on f.film_id = i.film_id
left join film_category fc on fc.category_id =f.film_id
left join category ca on ca.category_id = fc.category_id
where ca.name = 'Sci-Fi'
-- EX 8
select c.first_name, f.title, r.rental_date, r.return_date
from customer c 
left join rental r on c.customer_id = r.customer_id
left join inventory i on i.inventory_id = r.inventory_id
left join film f on f.film_id = i.film_id
where   r.return_date > (r.rental_date + INTERVAL '1 day' * f.rental_duration);
-- EX 9
select f.title, c1.first_name, c2.first_name
from film f
left join inventory i on f.film_id = i.film_id
left join rental r1 on i.inventory_id = r1.inventory_id
left join rental r2 on i.inventory_id = r2.inventory_id
left join customer c1 on r1.customer_id = c1.customer_id
left join customer c2 on r2.customer_id = c2.customer_id
where c2.customer_id > c1.customer_id;

select f.title, r.rental_date
from film f
left join inventory i on f.film_id = i.film_id
left join rental r on i.inventory_id = r.inventory_id