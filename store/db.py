from .store import Store

class DataBase:

    def __init__(self, filename):
        self._filename = filename

    def load_data(self):
        with open(self._filename) as file:
            file.readline()
            [Store(*el.strip().split(';')) for el in file]

    def save_data(self, stores, filename=None):
        pass