-- Retrieve:
--   - the 'id' and 'name' from the 'cities' table
--   - the 'name' from the 'states' table
-- Only include rows where the city's state_id matches the state's id (join condition)
-- Sort the results by 'cities.id' in ascending order
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
