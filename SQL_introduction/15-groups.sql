-- Count how many times each score value appears in 'second_table'
-- Group the results by score, so each unique score is listed once
-- The results are sorted in descending order by the score value
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
