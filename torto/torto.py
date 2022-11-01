from pathlib import Path

from tortoise.models import Model
from tortoise import fields, Tortoise


class Movie(Model):
    title = fields.CharField(max_length=255)
    year = fields.SmallIntField()
    score = fields.DecimalField(max_digits=2, decimal_places=2)

async def db_init():
    database_file = Path('db.sqlite3')
    if database_file.exists():
        database_file.unlink()
    await Tortoise.init(
        db_url='sqlite://[database_file]',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()

async def main():
    await Movie.create(title='The Matrix', year=1999, score=9.5)
    movie = Movie(title='And now for something completely different', year=1971, score=8.5)
    await movie.save()

    for movie in await Movie.all().only('score'):
        print(f'Elokuvan arvosana: {movie.score}')

db_init()
