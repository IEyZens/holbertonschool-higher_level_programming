-- Retrieve the top 10 rows from 'second_table' based on the highest 'score' values
-- The results are ordered in descending order by 'score'
-- Column names in the output will reflect the actual case used in the table definition
SELECT score, name FROM second_table ORDER BY SCORE DESC LIMIT 10;
