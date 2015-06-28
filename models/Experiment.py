from db.db import Database
import requests, config

class Experiment:
    def __init__(self, id=None, data=None):
        self._db = Database()

        if id: self._populate()
        else: self._new()

        if data: self.update(data)

    def update(self, data):
        result = self._db.cursor.execute(
            'UPDATE experiments SET (%s) = (%s) WHERE experiment_id = %s',
            (data.keys(), data.values(), self.id)
        )

        if result:
            self.data = data

        self._db.commit().close()

    def convert(self, ip2=None):
        if not self.data['files']: return

        requests.get(
            config.convert_url, { 'files': self.data['files'] }
        )

        # if we're passed ip2 instance then initiate search once conversion
        # is finished
        if ip2:
            poll(
                self.check_convert_status,
                lambda status: if 'success' in status return True,
                30,
                3600
            )

    def get_convert_status(self):
        return requests.get(config.convert_status_url, {
            'name': self.name
        })

    def search(self, ip2):

    def status(self):

    def remove(self):
        self._db.cursor.execute(
            'DELETE FROM experiments WHERE experiment_id = %s',
            (self.id, )
        )

        self._db.commit().close()

    def _populate(self):
        result = self._db.dict_cursor.execute(
            'SELECT * FROM experiments WHERE experiment_id = %s'
            (self.id, )
        )

        self.data = result
        self._db.commit().close()

    def _new(self):
        self._db.cursor.execute(
            'INSERT INTO experiments RETURNING experiment_id'
        )

        self.id = self._db.cursor.fetchone()[0]
        self._db.commit().close()