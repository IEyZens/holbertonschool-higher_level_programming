-- Select the title of each TV show and the name of its associated genre (if any)
-- Include all TV shows, even those without associated genres
-- Match each show with its genre(s) through the linking table tv_show_genres
-- Join genre information (if available) based on genre_id
-- Sort the results alphabetically by TV show title,
-- then by genre name in ascending order (NULLs last)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
