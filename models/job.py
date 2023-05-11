from db.db import sql

def all_jobs():
    return sql('SELECT * FROM jobs ORDER BY id')