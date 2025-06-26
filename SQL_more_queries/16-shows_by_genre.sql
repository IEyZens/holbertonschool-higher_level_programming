-- Select the title of each TV show and its associated genre_id
-- Use a LEFT JOIN to ensure all TV shows are included,
-- even those that do not have any associated genres (genre_id will be NULL in that case)
-- Sort the results first alphabetically by TV show title,
-- then by genre_id in ascending order (NULLs appear last by default)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
