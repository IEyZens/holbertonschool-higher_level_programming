-- Retrieve up to 10 rows from 'second_table' where the score is greater than or equal to 10
-- The results are ordered from highest to lowest score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY SCORE DESC LIMIT 10;
