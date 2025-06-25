-- Select all columns from the 'cities' table
-- Only include rows where the 'state_id' matches the 'id' of the state named 'California'
-- Results are sorted by 'id' in ascending order
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC
