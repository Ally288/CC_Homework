import sqlite3
import os

# this code generally stays the same but line 7 likely to change
# telling python where the file is - first two lines
def get_db():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, "task_manager.db")
    conn = sqlite3.connect(db)
    conn.execute(
        "PRAGMA foreign_keys = 1"
    )  # when there is foreign key, this brings it in
    conn.row_factory = sqlite3.Row
    return conn


def run_sql(sql, values=[]):
    db = get_db()
    cursor = db.cursor()  # looks throug all the rows
    cursor.execute(sql, values)  # holds onto the data
    results = cursor.fetchall()  # brings back all data
    db.commit()
    db.close()
    return results
