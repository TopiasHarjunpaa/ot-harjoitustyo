from entities.save import Save
from database_connection import get_database_connection


class SaveRepository:

    def __init__(self, connection):
        self._conn = connection

    def create(self, nickname):
        cursor = self._conn.cursor()
        sql = "INSERT INTO saves (nickname, progress, created_at) VALUES (?, 0, date())"
        cursor.execute(sql, (nickname,))
        self._conn.commit()
        return self.find_by_id(cursor.lastrowid)

    def update(self, progress, id):
        cursor = self._conn.cursor()
        sql = "UPDATE saves SET progress = ? WHERE id = ?"
        cursor.execute(sql, (progress, id))
        self._conn.commit()

    def find_by_id(self, id):
        cursor = self._conn.cursor()
        sql = "SELECT * FROM saves WHERE id = ?"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is not None:
            return Save(result[0], result[1], result[2], result[3])
        return None

    def find_all_saves(self):
        cursor = self._conn.cursor()
        sql = "SELECT * FROM saves ORDER BY progress DESC LIMIT 8"
        cursor.execute(sql)
        rows = cursor.fetchall()
        save_list = []
        for row in rows:
            save = Save(row[0], row[1], row[2], row[3])
            save_list.append(save)
        return save_list

    def delete(self):
        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM saves")
        self._conn.commit()


save_repository = SaveRepository(get_database_connection())
