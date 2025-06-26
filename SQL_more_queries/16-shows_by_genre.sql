-- Retrieve all TV shows and their associated genre IDs (if any)
-- Use a LEFT JOIN to include shows even if they have no genre associated
-- Sort the results alphabetically by show title, and by genre_id (NULLs will appear last)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
