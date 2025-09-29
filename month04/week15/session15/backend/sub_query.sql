-- 1
select film_id 
from film_actor
where actor_id = (
	select actor_id 
	from actor 
	where
	first_name = 'Penelope'
	and
	last_name = 'Guiness'
	)

-- 2
select title
from film
where film_id IN (
	select film_id
	from actor 
	where
	first_name = 'Penelope'
	and
	last_name = 'Guiness'
	)

-- 3
select  
f.title
from film f
where exists (
	select 
	1
	from inventory i
	join rental r on r.inventory_id = i.inventory_id 
	where i.film_id = f.film_id
) order by f.title

-- 4
select first_name, last_name
from customer
where address_id not in (
		select
		address_id
	from address
	where city_id in (
		select 
			city_id
		from city
		where country_id = (
			select 
				country_id
			from country
			where country = 'Canada'
        )
    )     
)

-- 5
select 
select first_name, last_name, 
(select count(*) from rental r where r.customer_id = c.customer_id) as rental_count
from customer c

-- 6 
select first_name, last_name 
from actor a
where (select count(film_id) from film_actor fa where fa.actor_id = a.actor_id ) > 30
-- Other variation
select first_name, last_name from actor 
	where actor_id in (
	select actor_id
	from film_actor 
	group by actor_id 
	having count(film_id) > 30
)

-- 7
select
p1.customer_id,
p1.amount,
p1.payment_date
from payment p1 
where
p1.payment_date = (
	select max(p2.payment_date )
	from payment p2
	where p2.customer_id = p1.customer_id
);

-- 8
select title, length
from film 
where length > any (
	select f.length
	from film f
	join film_category fc on fc.film_id = f.film_id
	join category c on fc.category_id = c.category_id
	where c.name = 'Action'
)

-- 9
select title, length
from film 
where length > all  (
	select f.length
	from film f
	join film_category fc on fc.film_id = f.film_id
	join category c on fc.category_id = c.category_id
	where c.name = 'Action'
);

-- 10
select 
	f.title,
	rental_counts.count
from 
	(select 
		i.film_id,
		count(r.rental_id) as count
	from 
		rental r
	join inventory i on r.inventory_id = i.inventory_id 
	group by i.film_id 
	order by
		count desc
	limit 10
	) as rental_counts
join film f 
on f.film_id = rental_counts.film_id

-- 11
select distinct
	customer_id
from payment  
where amount < (
	select 
	avg(amount)
	from payment
)

--  12
select count(*)
from film 
where film_id not in (
	select 
		fc.film_id
	from film_category fc 
	join category c
	on fc.category_id = c.category_id
	where c.name = 'Family'
)

-- 13
select
	distinct 
	c.email
from customer c
join rental r on c.customer_id = r.customer_id
join inventory i on r.inventory_id = i.inventory_id
where i.film_id in (
	select film_id 
	from film
	where length > (
		select avg(length) from film
	)
)

