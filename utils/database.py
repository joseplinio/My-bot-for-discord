import sqlite3

def init_db():
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            inventory TEXT
        )
    """)
    conn.commit()
    conn.close()
