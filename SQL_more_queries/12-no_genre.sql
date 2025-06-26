-- Retrieve titles of TV shows that have no associated genres
-- Use a LEFT JOIN to include all TV shows, then filter those where no match was found in 'tv_show_genres'
-- Sort the result by title and genre_id (which will be NULL)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
