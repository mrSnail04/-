import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

conn = psycopg2.connect(dbname="northwind", user="postgres", password="Vfrcbv0405")

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS superheroes')

cur.execute('CREATE TABLE superheroes(hero_id serial PRIMARY KEY, hero_name varchar, strength int);')

cur.execute('DROP TABLE IF EXISTS superheroes')

conn.commit()

cur.execute('CREATE TABLE superheroes(hero_id serial PRIMARY KEY, hero_name varchar, strength int);')

cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES(%s, %s)", ("Flash", 10))

cur.execute("""
            INSERT INTO superheroes (hero_name, strength) 
            VALUES(%(name)s, %(strength)s);
            """, {"name": "Superman", "strength": 100})

conn.commit()

cur.execute("SELECT * FROM superheroes")

one_list = cur.fetchone()
print(one_list)

full_fetch = cur.fetchall()

for record in full_fetch:
    print(full_fetch)

conn.commit()

cur.close()

conn.close()

with psycopg2.connect(dbname="northwind", user="postgres", password="Vfrcbv0405") as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        execute_values(curs, """
                             INSERT INTO superheroes (hero_name, strength)
                             VALUES %s;
                             """, [("Batman", 15), ("Arrow", 15), ("Supergirl", 54)])
        curs.execute("SELECT * FROM superheroes")
        records = curs.fetchall()
        print(records)
        print(records[2]['hero_name'])

conn = psycopg2.connect(dbname="northwind", user="postgres", password="Vfrcbv0405")
with conn:
    with conn.cursor() as curs:
        curs.execute("""
                    UPDATE superheroes
                    SET strength = %s
                    WHERE hero_name = %s
                    """, (90, 'Superman'))
with conn:
    with conn.cursor() as curs:
        curs.execute("SELECT * FROM superheroes")
        print(curs.fetchall())