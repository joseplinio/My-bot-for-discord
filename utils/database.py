import sqlite3


def init_db():
    global conn
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            count INTEGER
        )
    """)
    conn.commit()

def create_user(id, count):
    c = conn.cursor()
    c.execute("")

    conn.commit()