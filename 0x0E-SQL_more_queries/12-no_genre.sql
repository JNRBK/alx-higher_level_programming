-- lists all shows contained in hbtn_0d_tvshows
-- without genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = (SELECT * FROM tv_show_genres WHERE genre_id IS NULL)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;