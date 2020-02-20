import sqlite3
from contextlib import contextmanager


DB = 'storage_project_db.db'
@contextmanager
def access_db():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()