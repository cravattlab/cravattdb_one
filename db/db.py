import psycopg2, psycopg2.extras, config

class Database:
    def __init__(self, templates=None):
        self.connection = psycopg2.connect(
            database = config.PGSQL_DATABASE_NAME,
            user = config.PGSQL_DATABASE_USER,
            password = config.PGSQL_DATABASE_PASSWORD,
            host = config.PGSQL_DATABASE_HOSTNAME
        )

        self.cursor = self.connection.cursor()

        self.dict_cursor = self.connection.cursor(
            cursor_factory = psycopg2.extras.RealDictCursor
        )

        if templates: self.__templates = templates

        return self

    def close(self):
        self.cursor.close()
        self.dict_cursor.close()

    def commit(self):
        self.connection.commit()
        return self

    def get_sql(self, template, data):
        with open(self.__templates[template]) as f:
            return f.read()