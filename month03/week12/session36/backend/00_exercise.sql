insert into actor (first_name, last_name) values ('Chinggis', 'Khaan')
select actor_id, first_name, last_name from actor where first_name = 'Chinggis'

insert into category (name) 
values('Biopic')

update actor set last_name='Khan' where actor_id= 204

update film set rental_duration = rental_duration+1

select rental_duration from film where film_id = 5

delete from actor where actor_id=204

delete from customer where customer_id = 1

insert into language (name) values('Mongolian')
insert into country (country) values('Mongolia')
insert into city(city, country_id) values('Ulaanbaatar', 110)

UPDATE film f SET rental_rate = f.rental_rate + 0.5
FROM film_category fc
JOIN category c ON fc.category_id = c.category_id
WHERE f.film_id = fc.film_id AND c.name = 'Horror';
