import psycopg2, config

class Database:
    def __init__():
        self.connection = psycopg2.connect(
            database = config.PGSQL_DATABASE_NAME,
            user = config.PGSQL_DATABASE_USER,
            password = config.PGSQL_DATABASE_PASSWORD
        )

        self.cursor = connection.cursor()

    def close():
        self.cursor.close()
        self.connection.close()