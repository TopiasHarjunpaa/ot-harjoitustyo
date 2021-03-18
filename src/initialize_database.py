from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    # Just for testing purposes right now...
    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS results;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    # Just for testing purposes right now...
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE results (
            id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            points INTEGER,
            time TIMESTAMP
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
