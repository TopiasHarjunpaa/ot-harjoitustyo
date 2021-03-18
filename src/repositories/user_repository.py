from entities.user import User
from database_connection import get_database_connection


class UserRepository:

    def __init__(self, connection):
        self._conn = connection

    def create(self, username, password):
        cursor = self._conn.cursor()
        sql = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(sql, (username, password))
        self._conn.commit()

    def find_user_by_username(self, username):
        cursor = self._conn.cursor()
        sql = "SELECT id, username, password FROM users WHERE username = ?"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        if result is not None:
            return User(result[1], result[2], result[0])
        return None

    def find_all_users(self):
        cursor = self._conn.cursor()
        sql = "SELECT id, username, password FROM users"
        cursor.execute(sql)
        results = cursor.fetchall()
        user_list = []
        for result in results:
            user = User(result[1], result[2], result[0])
            user_list.append(user)
        return user_list


user_repository = UserRepository(get_database_connection())
