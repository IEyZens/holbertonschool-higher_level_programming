-- Select the id, name, and state_id of cities that belong to the state named 'California'
-- Filter to include only cities where the state_id matches the id of the state 'California'
-- Sort the results by city id in ascending order
SELECT cities.id, cities.name, cities.state_id
FROM cities
WHERE state_id = (SELECT cities.id FROM states WHERE name = 'California')
ORDER BY cities.id ASC
