from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    # No use for first two tables...Needs to be removed.
    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS results;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS saves;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    # No use for first two tables...Needs to be removed.
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
    cursor.execute('''
        CREATE TABLE saves (
            id INTEGER PRIMARY KEY,
            nickname TEXT,
            progress INTEGER,
            created_at TIMESTAMP,
            ed_at TIMESTAMP
        );
    ''')
    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
