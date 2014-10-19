from db.db import Database

class Dataset:
    def __init__(self, id):
        self.__db = Database()
        self.id = id

    def bootstrap(self):
        return {
            'dataset': self.fetch_dataset()
        }

    def fetch_dataset(self):
        results = {}

        sql = 'SELECT peptide_index, ipi, symbol, sequence, ratio FROM {0}'.format('experiment_' + str(self.id))

        self.__db.cursor.execute(sql)
        self.__db.connection.commit()

        results['data'] = self.__db.cursor.fetchall()
        results['headers'] = [ desc[0] for desc in self.__db.cursor.description ]

        self.__db.close()

        return results