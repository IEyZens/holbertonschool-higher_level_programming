-- Retrieve the name of each genre and the number of shows associated with it
-- Join 'tv_show_genres' and 'tv_genres' using the genre ID
-- Group by genre name to count how many times each genre appears in the linking table
-- Sort the result by the number of shows in descending order (most popular genres first)
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres, tv_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC
