-- Retrieve the titles of all TV shows that are associated with the genre "Comedy"
-- Join tv_shows, tv_show_genres (link table), and tv_genres
-- Filter on the genre name being "Comedy"
-- Sort the results alphabetically by the show title
SELECT tv_shows.title
FROM tv_shows, tv_genres, tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id AND tv_show_genres.genre_id = tv_genres.id AND tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC
