import sqlite3

DATABASE_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, 0))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = [{"id": row[0], "task": row[1], "completed": bool(row[2])} for row in cursor.fetchall()]
    conn.close()
    return tasks

def mark_task_completed(task_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (1, task_id))
    conn.commit()
    conn.close()
