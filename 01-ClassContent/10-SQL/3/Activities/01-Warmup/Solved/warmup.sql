SELECT address, city
FROM address a
JOIN city c
ON (a.city_id = c.city_id);

SELECT address, city
FROM address
JOIN city
USING (city_id);
