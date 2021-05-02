from entities.save import Save
from database_connection import get_database_connection


class SaveRepository:
    """A class to represent save repository and to handle SQL-queries.

    Attributes:
        connection: A SQLite database connection.
    """

    def __init__(self, connection):
        """Constructs connection to the save repository object.

        Args:
            connection (sqlite3.Connection): A SQLite database connection.
        """

        self._conn = connection

    def create(self, nickname):
        """Creates new save into database.

        Args:
            nickname (str): Name of the save object.

        Returns:
            save (Save): Calls find_by_id -method which creates save object
            according to the id number recieved from SQL-query.
        """

        cursor = self._conn.cursor()
        sql = "INSERT INTO saves (nickname, progress, created_at) VALUES (?, 0, date())"
        cursor.execute(sql, (nickname,))
        self._conn.commit()
        return self.find_by_id(cursor.lastrowid)

    def update(self, progress, save_id):
        """Updates existing save at the database

        Args:
            progress (int): Corresponds progress level of the game.
            save_id (int): Unique id number.
        """

        cursor = self._conn.cursor()
        sql = "UPDATE saves SET progress = ? WHERE id = ?"
        cursor.execute(sql, (progress, save_id))
        self._conn.commit()

    def find_by_id(self, save_id):
        """Finds save from the database according to save id.

        Args:
            save_id (int): Unique id number.

        Returns:
            save (Save): Returns save if user_id exists in database
            save (None): Returns none if user_id does not exist.
        """

        cursor = self._conn.cursor()
        sql = "SELECT * FROM saves WHERE id = ?"
        cursor.execute(sql, (save_id,))
        result = cursor.fetchone()
        if result is not None:
            return Save(result[0], result[1], result[2], result[3])
        return None

    def find_all_saves(self):
        """Finds 8 saves from the database sorted by highest progress.

        Returns:
            save_list (list): Returns list of save objects.
        """

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
        """Deletes saves from the database.
        """

        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM saves")
        self._conn.commit()


save_repository = SaveRepository(get_database_connection())
