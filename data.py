import sqlite3

conn = sqlite3.connect("data.db")


def init():
    # Create Table for Tasks
    # TODO: Date has to be checked still...
    conn.execute("CREATE TABLE IF NOT EXISTS task ("
                 "task_id INTEGER PRIMARY KEY ASC,"
                 "timestamp DATETIME DEFAULT CURRENT_DATE NOT NULL, done INT DEFAULT 0 NOT NULL,"
                 "important INT DEFAULT 0 NOT NULL,"
                 "due_date DATE NOT NULL CHECK (due_date=STRFTIME('%d-%m-%Y', due_date)),"
                 "description TEXT NOT NULL, category_id INTEGER NULL)")
    # Create Table for Category
    conn.execute("CREATE TABLE IF NOT EXISTS "
                 "category (category_id INTEGER PRIMARY KEY ASC,"
                 "category_name TEXT NOT NULL)")


def add_task(description, due_date, important=0):
    conn.execute("INSERT INTO task (description, due_date, important) VALUES (?, ?, ?)", [description, due_date, important])
    conn.commit()


def remove_task(task_id):
    conn.execute("DELETE FROM task WHERE task_id=?", [task_id])
    conn.commit()


def add_category(name):
    conn.execute("INSERT INTO category (category_name) VALUES(?)", [name])
    conn.commit()


def remove_category(category_id):
    # TODO: Also remove ID in Task
    conn.execute("DELETE FROM category WHERE category_id=?", [category_id])
    conn.commit()


# TODO: David - Category Update, Oguzhan - Task Update

init()

# add_task("Fegen", "02.02.2018")