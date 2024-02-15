-- lists all shows contained in hbtn_0d_tvshows that have
-- atleast one genre linked
-- each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres
ORDER BY tv_shows.title, tv_show_genres.genre_id;