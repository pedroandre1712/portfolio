USE sakila;

-- Questao 1

SELECT  A.film_id,
        A.title,
        A.description,
        A.release_year,
        A.language_id,
        A.original_language_id,
        A.rental_duration,
        A.rental_rate,
        A.length,
        A.replacement_cost,
        A.rating,
        A.special_features,
        A.last_update,
        B.actor_id,
        B.last_update,
        C.category_id,
        C.last_update,
        D.title,
        D.description
FROM (((film as A
INNER JOIN film_actor as B
	ON A.film_id = B.film_id)
INNER JOIN film_category as C
	ON A.film_id = C.film_id)
INNER JOIN film_text as D
	ON A.film_id = D.film_id);

-- Questao 2
SELECT A.first_name as nome, 
	   A.last_name as sobrenome, 
       A.email, 
       C.city 
FROM customer as A
INNER JOIN address as B
	on A.address_id = B.address_id
INNER JOIN city as C
	on B.city_id = C.city_id
INNER JOIN payment as P
	USING (customer_id)
    group by P.customer_id
    having count(P.amount)>40;

-- Questao 3
SELECT * 
FROM inventory
INNER JOIN film as f
	USING(film_id)
;
-- Questao 4
SELECT SUM(amount) as total_pagamento FROM sakila.payment
INNER JOIN rental
	USING(rental_id)
WHERE rental.return_date is NULL;
