-- Retrieve a list of all TV shows from the database
-- Before running this, create a new database named 'hbtn_0d_tvshows'
-- Import the SQL data into the 'hbtn_0d_tvshows' database
-- Switch to the 'hbtn_0d_tvshows' database using the 'USE' statement
-- You can use the 'source' command to execute the SQL script: source hbtn_0d_tvshows.sql
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;

