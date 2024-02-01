-- List the names of all people who starred in a movie released in 2004
SELECT DISTINCT name FROM people p
JOIN stars s on s.person_id = p.id
JOIN movies m on m.id = s.movie_id
WHERE m.year = 2004
ORDER BY p.birth;
