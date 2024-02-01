# given the name of movie, list all actors who star in it

import sys 
import sqlite3
import re 

# globals 
usage = f'Usage: python3 starring.py "[movie_title]"'
db = None 

# process command-line arguments 
argc = len(sys.argv)
if argc != 2:
    print(usage)
    exit(1)
movie = sys.argv[1] 

# execute query 
try: 
    db = sqlite3.connect("movies.db")
    cur = db.cursor()

    cur.execute("select * from Movies where title = ? COLLATE NOCASE", (movie,))
    isValidMovie = cur.fetchall()
    if not isValidMovie:
        print("The input does not exist")
        exit(1) 
    elif len(isValidMovie) > 1:
        year = input("Release year of movie: ")
        year = int(year)
        cur.execute("select * from Movies where title = ? COLLATE NOCASE and year = ?", (movie, year))
        if not cur.fetchone():
            print(f"No movie with the selected title came out in {year}")
            exit(1)
    else: 
        year = int(isValidMovie[0][2])

    cur.execute(
        """
        SELECT p.name
        FROM people p
        JOIN stars s ON s.person_id = p.id
        JOIN movies m ON m.id = s.movie_id
        WHERE m.title = ? COLLATE NOCASE AND m.year = ?
        ORDER BY p.name
        """, (movie, year,)
    )

    res = cur.fetchall()  
    for tup in res:
        print(tup[0])

except Exception as err:
    print(err)
finally:
    if db:
        db.close()
