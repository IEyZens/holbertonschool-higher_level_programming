-- Retrieve all rows from 'second_table' where:
--   - 'name' is not NULL
--   - 'name' is not an empty string
-- Sort the results in descending order by 'score'
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
