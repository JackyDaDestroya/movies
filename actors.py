# given an actor's name, find the movies that have starrred in 

import sys 
import sqlite3
import re 

# globals 

usage = f"Incorrect Usage: input an actor's first and last name"
db = None 

# process command-line arguments 

argc = len(sys.argv)
if argc != 3:
    print(usage)
    exit(1)
actor = sys.argv[1] + " " + sys.argv[2]


# execute query 

try: 
    db = sqlite3.connect("movies.db")
    cur = db.cursor()

    cur.execute("select * from People where name = ?", (actor,))
    isValidActor = cur.fetchone()
    if not isValidActor:
        print("The actor you have inputted does not exist")
        exit(1) 
        

    cur.execute(
        """
        SELECT m.title, m.year
        FROM movies m 
        JOIN stars s ON s.movie_id = m.id
        JOIN people p ON p.id = s.person_id
        WHERE p.name = ?
        ORDER BY m.year
        """, (actor,)
    )

    res = cur.fetchall()
    for tup in res:
        print(str(tup[1]) + " - " + tup[0])

except Exception as err:
    print(err)
finally:
    if db:
        db.close()
