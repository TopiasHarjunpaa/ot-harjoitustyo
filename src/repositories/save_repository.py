from entities.save import Save
from database_connection import get_database_connection

# TODO: Find a way to deal with the same nicknames... Handle exception or search by id instead?


class SaveRepository:

    def __init__(self, connection):
        self._conn = connection

    def create(self, nickname):
        cursor = self._conn.cursor()
        sql = "INSERT INTO saves (nickname, progress, created_at) VALUES (?, 0, datetime())"
        cursor.execute(sql, (nickname,))
        self._conn.commit()

    def find_by_nickname(self, nickname):
        cursor = self._conn.cursor()
        sql = "SELECT * FROM saves WHERE nickname = ?"
        cursor.execute(sql, (nickname,))
        result = cursor.fetchone()
        if result is not None:
            return Save(result[1], result[2], result[3])
        return None

    def find_all_saves(self):
        # TODO: Filter max 9 results and rank with highest progress.
        cursor = self._conn.cursor()
        sql = "SELECT * FROM saves"
        cursor.execute(sql)
        rows = cursor.fetchall()
        save_list = []
        for row in rows:
            save = Save(row[1], row[2], row[3])
            save_list.append(save)
        return save_list

    def delete(self):
        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM saves")
        self._conn.commit()


save_repository = SaveRepository(get_database_connection())
