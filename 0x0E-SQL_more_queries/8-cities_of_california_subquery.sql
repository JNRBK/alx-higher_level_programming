-- lists the cities of California that can be
-- found in the database hbtn_0d_usa
SELECT * FROM cities WHERE name = "California"
ORDER BY cities.id ASC;