select * from actor;


-- desc, asc
select * from actor order by first_name desc;

-- first_name , last_name

select * from actor order by first_name, last_name desc;
select * from actor order by first_name desc, last_name asc

select * from actor order by actor_id desc

-- film data
select * from film;

select title, length from film order by length desc;


select * from film order by replacement_cost asc;

select title, rental_rate from film order by rental_rate  desc limit 1;

select rental_rate from film order by rental_rate asc limit 1;

select distinct replacement_cost from film order by replacement_cost;

-- IN
select * from city c;

select * from city where city in ('Brest', 'Brindisi', 'Callao');

select * from city where city = 'Brest' or city = 'Brindisi' or city = 'Callao'
