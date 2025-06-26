-- Retrieve:
--   - the title of each TV show from 'tv_shows'
--   - the genre_id from 'tv_show_genres' if it exists
-- Include all TV shows, even those without any associated genres (LEFT JOIN)
-- Sort the results by title (A-Z), then by genre_id (lowest to highest)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
