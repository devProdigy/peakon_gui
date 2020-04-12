import sqlite3


TABLE_NAME = "quiz"


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        # self.cur.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")  # TODO clear table

        self.cur.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} "
            "(id INTEGER PRIMARY KEY, question text, score integer, comment text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = self.cur.fetchall()
        return rows

    def insert(self, question: str, score: int, comment: str):
        self.cur.execute(f"INSERT INTO {TABLE_NAME} VALUES (NULL, ?, ?, ?)", (question, score, comment))
        self.conn.commit()

    def clear_db(self):
        self.cur.execute(f"DELETE FROM {TABLE_NAME}")
        self.conn.commit()
        self.cur.execute("VACUUM")
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db_instance = Database('quiz_db.sqlite')
