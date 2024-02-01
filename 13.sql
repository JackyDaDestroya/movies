-- List the names of all people who starred in a movie in which Kevin Bacon also starred 
SELECT DISTINCT p.name FROM people p
JOIN stars s on s.person_id = p.id
JOIN movies m on m.id = s.movie_id
WHERE p.name != 'Kevin Bacon' AND m.title IN
(
SELECT m.title FROM people p
JOIN stars s on s.person_id = p.id
JOIN movies m on m.id = s.movie_id
WHERE p.name = 'Kevin Bacon' AND p.birth = 1958
);
