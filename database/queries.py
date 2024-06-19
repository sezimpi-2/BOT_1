class Queries:
    CREATE_SURVEY_TABLE="""
CREATE TABLE IF NOT EXISTS  survey_results(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
date TEXT,
instagram TEXT,
meals  TEXT,
purity TEXT )

  """
    DROP_MEALS_TABLE = "DROP TABLE IF EXISTS meals"
    DROP_CAFFE_TABLE = "DROP TABLE IF EXISTS caffe"
    CREATE_MEALS_TABLE = """
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
CREATE_CAFFE_TABLE = """
        CREATE TABLE IF NOT EXISTS caffe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            image TEXT,
            meals_id INTEGER,
            FOREIGN KEY (meals_id) REFERENCES meals(id)
        ) 
    """
POPULATE_MEALS = """
        INSERT INTO meals (name)
        VALUES ("Пасты"),
        ("Напитки"),
        ("Пиццы"),
    """
POPULATE_CAFFE = """
        INSERT INTO caffe (name, price, image, meals_id)
        VALUES ("Пицца с мексиканским соусом", 200, "images/traditsionnie-bluda-italii.jpg", 1),
        ("Популярное блюдо италии", 2000, "images/7aad.jpg", 3),
        ("Паста", 2000, "images/resti.jpg", 3)
    """
