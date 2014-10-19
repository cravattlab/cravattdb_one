from db.db import Database

class List:
    def __init__(self):
        self.__db = Database()

    def bootstrap(self):
        return {
            'list': self.fetch_all()
        }

    def fetch_all(self):
        results = {}

        sql = 'SELECT * FROM experiments_view'
        
        self.__db.cursor.execute(sql)
        self.__db.connection.commit()

        results['data'] = self.__db.cursor.fetchall()
        results['headers'] = [ desc[0] for desc in self.__db.cursor.description ]

        self.__db.close()

        return results