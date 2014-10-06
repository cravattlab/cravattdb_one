import psycopg2, psycopg2.extras, config

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            database = config.PGSQL_DATABASE_NAME,
            user = config.PGSQL_DATABASE_USER,
            password = config.PGSQL_DATABASE_PASSWORD
        )

        self.cursor = self.connection.cursor()

        self.dict_cursor = self.connection.cursor(
            cursor_factory = psycopg2.extras.RealDictCursor
        )

    def close(self):
        self.cursor.close()
        self.connection.close()