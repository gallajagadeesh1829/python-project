import sqlite3
from pathlib import Path

DB_PATH = Path("data/app.db")


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)


def add_task(title: str):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,),
        )


def get_tasks():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(
            "SELECT id, title, completed FROM tasks ORDER BY id DESC"
        ).fetchall()