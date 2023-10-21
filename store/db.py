from .store import Store

class DataBase:

    def __init__(self, filename):
        self._filename = filename

    def load_data(self):
        pass # TODO: Read data from csv file and store in db

    def save_data(self, stores, filename=None):
        pass