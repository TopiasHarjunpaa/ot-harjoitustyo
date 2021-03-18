from entities.result import Result
from database_connection import get_database_connection


class ResultRepository:

    def __init__(self, connection):
        self._conn = connection

    def create(self, user_id, points):
        cursor = self._conn.cursor()
        sql = "INSERT INTO results (user_id, points, time) VALUES (?, ?, datetime())"
        cursor.execute(sql, (user_id, points))
        self._conn.commit()

    def find_all_results(self):
        cursor = self._conn.cursor()
        sql = "SELECT * FROM results"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result_list = []
        for row in rows:
            result = Result(row[1], row[2], row[3], row[0])
            result_list.append(result)
        return result_list


result_repository = ResultRepository(get_database_connection())
