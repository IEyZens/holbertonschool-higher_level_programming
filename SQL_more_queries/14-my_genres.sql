-- Retrieve the names of all genres associated with the TV show titled "Dexter"
-- Join the three tables: tv_shows, tv_show_genres (linking table), and tv_genres
-- Match where:
--   - tv_show_genres references the show via show_id
--   - tv_show_genres references the genre via genre_id
--   - the show title is "Dexter"
-- Sort the genre names in alphabetical order
SELECT tv_genres.name
FROM tv_shows, tv_genres, tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id AND tv_show_genres.genre_id = tv_genres.id AND tv_shows.title = "Dexter"
ORDER BY name ASC
