-- Retrieve:
--   - the title of each TV show from 'tv_shows'
--   - the genre_id from the linking table 'tv_show_genres'
-- Match only rows where:
--   - tv_show_genres.show_id matches tv_shows.id
--   - tv_show_genres.genre_id matches tv_genres.id
-- Sort the results alphabetically by tv show title, then by genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_genres, tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
