class Queries:
    CREATE_SURVEY_TABLE="""
CREATE TABLE IF NOT EXISTS  survey_results(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
date TEXT,
instagram TEXT,
meals  TEXT,
purity TEXT )"""
