import aiosqlite 
from database.queries import Queries 
 
class Database: 
    def __init__(self, path): 
        self.path = path 
 
    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            # создание всех таблиц
            await conn.execute(Queries.CREATE_SURVEY_TABLE)
            await conn.execute(Queries.DROP_MEALS_TABLE)
            await conn.execute(Queries.DROP_CAFFE_TABLE)
            await conn.execute(Queries.CREATE_MEALS_TABLE)
            await conn.execute(Queries.CREATE_CAFFE_TABLE)
            await conn.execute(Queries.POPULATE_MEALS)
            await conn.execute(Queries.POPULATE_CAFFE)
            # здесь может быть создание других таблиц
            # которые нам нужны
            await conn.commit()
    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query,params)
            await conn.commit()









