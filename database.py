import sqlite3
import hashlib

DATABASE_NAME = "tasks.db"

def init_db():

    print("Initializing the database.")
    # Rest of the code to create the tables

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            completed INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    


def get_user(username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        user = {
            "id": user_data[0],
            "username": user_data[1],
            "password": user_data[2]
        }
        return user
    else:
        return None



def get_user_by_id(user_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        user = {
            "id": user_data[0],
            "username": user_data[1],
            "password": user_data[2]
        }
        return user
    else:
        return None









def add_task(user_id, task):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_id, task, completed) VALUES (?, ?, ?)", (user_id, task, 0))
    conn.commit()
    conn.close()



def get_tasks(user_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = [{"id": row[0], "task": row[2], "completed": bool(row[3])} for row in cursor.fetchall()]
    conn.close()
    return tasks


def mark_task_completed(task_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (1, task_id))
    conn.commit()
    conn.close()





