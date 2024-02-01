-- List the names of all people who starred in Toy Story
SELECT name FROM people p
JOIN stars s ON s.person_id = p.id
JOIN movies m ON m.id = s.movie_id
WHERE m.title = 'Toy Story';
