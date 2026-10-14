import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "books.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT,
            year INTEGER,
            isbn TEXT
        )
    """)

    connection.commit()
    connection.close()