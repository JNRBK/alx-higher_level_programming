-- lists all cities contained in DB hbtn_0d_usa
-- each record should display cities.id - cities.name - states.name
-- can use only one SELECT
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ORDER BY cities.id ASC;