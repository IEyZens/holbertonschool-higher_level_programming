-- Query to list all TV shows with their genres, including those without any genres
-- Use a LEFT JOIN to include all TV shows, then filter those where no match was found in 'tv_show_genres'
-- Sort the result by title and genre_id (which will be NULL)
-- This query will return all TV shows, including those that have no associated genres
-- The WHERE clause is adjusted to include all shows, regardless of whether they have genres or not
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id OR tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
