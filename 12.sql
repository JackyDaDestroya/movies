-- List the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred
SELECT title FROM movies m
JOIN stars s ON s.movie_id = m.id
JOIN people p ON p.id = s.person_id
WHERE p.name = 'Bradley Cooper'

INTERSECT

SELECT title FROM movies m
JOIN stars s ON s.movie_id = m.id
JOIN people p ON p.id = s.person_id
WHERE p.name = 'Jennifer Lawrence';
