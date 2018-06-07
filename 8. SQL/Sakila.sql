# Homework 8
USE sakila;

#1a
SELECT last_name, first_name
from actor;
#1b
select upper(concat(last_name," ", first_name))
as 'Actor Name'
from actor;


#2a
select actor_id, first_name, last_name
from actor
where first_name like "Joe";
#2b
select * 
from actor
where last_name like '%GEN%';


#3a
alter table actor
add middle_name varchar(30) after first_name;
#3b
alter table actor
modify column middle_name blob(10);
#3c
alter table actor
drop column middle_name;



#4a
select distinct last_name, count(last_name)
from actor
group by last_name;
#4b
select distinct last_name, count(last_name) as Count
from actor
group by last_name
having count(last_name) > 1;
#4c
SET SQL_SAFE_UPDATES = 0;
update actor 
set first_name = 'HARPO'
where actor_id = 172;
#4d
update actor
set first_name = 'GROUCHO'
where first_name = 'HARPO'

#6a
select staff.first_name, staff.last_name, address.address
from staff
left join address
on staff.address_id = address.address_id;
#6b
select staff.first_name, staff.last_name, sum(payment.amount)
from staff
join payment
on staff.staff_id = payment.staff_id
group by payment.staff_id;
#6c
select film.title, count(film_actor.actor_id)
from film
inner join film_actor
on film.film_id = film_actor.film_id
group by film_actor.film_id;
#6d
select count(film_id)
from inventory 
where film_id = 
	(select film_id 
	from film
	where title = 'Hunchback Impossible'); # there exists 6
#6e
select customer.first_name, customer.last_name, sum(payment.amount)
from customer
join payment
on customer.customer_id = payment.customer_id;


#7a
select title
from film
where 
	(title like 'K%' or title like 'Q%')
	and 
    language_id = (select language_id
		from language
		where name = 'English');
#7b
select *
from actor
where actor_id in (
	select actor_id
	from film_actor
		where
		film_actor.film_id = (
			select film_id 
            from film 
				where title = 'Alone Trip'
			)
	);
#7c
select concat(first_name, " ", last_name), email
from customer
	where address_id in (
		select address_id
		from address
		where city_id in (
			select city_id
			from city
				where country_id = (
					select country_id
					from country
						where country = 'Canada'
					)
			)
		);
#7d
select title
 from film
 where film_id in (
	select film_id
    from film_category
		where category_id = (
			select category_id
            from category
				where name = 'Family'
			)
		);
#7e
select film_id, title
from film
where film_id in (
	select film_id
	from inventory
		where inventory_id in (
			select inventory_id
			from rental
			)
	order by count(film_id)
	);













