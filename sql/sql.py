import sqlite3

con = sqlite3.connect('db_conn.sqlite')

cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS movie')
cur.execute('CREATE TABLE IF NOT EXISTS movie(title, year, score)')

res = cur.execute('SELECT name FROM sqlite_master')
row = res.fetchone()
if row:
    print(f'Tietokonnassa on olemassa tama taulu: {row[0]}')
else:
    print(f'Tietokantaan ei ole luotu taulua')

cur.execute('''
    INSERT INTO movie VALUES
        ("Monthy Python and the Holy Grail", 1975, 8.2),
        ('And now fro something completely different', 1971, 7.6)
        '''
            )
con.commit()
res = cur.execute('SELECT * FROM movie')
for row in res.fetchall():
    score = row[0]
    print(f'Elokuvan arvosana on {score}')

data = [
    ('Monty Python Live at the Hollywood Bowl', 1982, 7.9),
    ('Monty Python and the Meaning of Life', 1983, 8.3),
    ("Monty Python's Life of Brian", 1979, 8.1),
]

cur.executemany('INSERT INTO movie VALUES (?,?,?)', data)
con.commit()

res = cur.execute('SELECT * FROM movie')
for title, year, score in res.fetchall():
    print(f'Elokuvan {title} vuodesta {year}')

#res = cur.execute('SELECT * MAX(score),title, year FROM movie')
res = cur.execute('SELECT * FROM movie ORDER BY score LIMIT 1')
title, year, score = res.fetchone()
print(f'Paras elokuva on {title} vuodelta {year} ja sen arvosana on {score}')
