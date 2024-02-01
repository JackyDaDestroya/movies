-- number of movies with an IMDb rating of 10.0
SELECT count(*) FROM movies m
JOIN ratings r ON r.movie_id = m.id
WHERE r.rating = 10;
