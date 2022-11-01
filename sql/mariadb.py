import mariadb
import sys

try:
    conn = mariadb.conn(
        user = 'root',
        password = '',
        host = 'localhost',
        port = 3306,
        database = 'harjoitus'
    )
except mariadb.Error as e:
    print(f'Error connecting to MariaDB Platform: {e}')
    sys.exit(1)

cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS movie('
            'title VARCHAR(255),'
            ' year SMALLINT,'
            ' score FLOAT)')

cur.execute('''
    INSERT INTO movie VALUES
        ("Monthy Python and the Holy Grail", 1975, 8.2),
        ('And now fro something completely different', 1971, 7.6)
    '''
        )
conn.commit()

cur.execute('SELECT score FROM movie')