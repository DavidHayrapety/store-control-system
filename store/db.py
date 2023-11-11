from .store import Store
from .product import Product


class DataBase:

    _store_headers = []
    _product_headers = []

    def __init__(self, store_data, product_data):
        self._store_data = store_data
        self._product_data = product_data

    def __load_store_data(self):
        with open(self._store_data) as file:
            self._store_headers = file.readline().strip().split(';')
            result = {header: [] for header in self._store_headers}
            count = 0
            for line in file:
                line = line.strip().split(';')
                count += 1
                for k, v in zip(self._store_headers, line):
                    result[k].append(v)
            return result, count

    def create_stores(self,):
        store_dict, count = self.__load_store_data()
        stores = []
        for i in range(count):
            dict = {header.lower(): store_dict[header][i]
                    for header in self._store_headers}
            stores.append(Store(**dict))
        return stores

    def save_store_data(self, stores, store_data=None):
        if store_data == None:
            with open(self._store_data, 'w') as file:
                file.write(';'.join(self._store_headers)+'\n')
                for store in stores:
                    details = []
                    for i in range(len(self._store_headers)):
                        details.append(
                            getattr(store, self._store_headers[i].lower()))
                    line = ';'.join(details)
                    file.write(line+'\n')
        else:
            with open(store_data, 'w') as file:
                file.write(';'.join(self._store_headers)+'\n')
                for store in stores:
                    details = []
                    for i in range(len(self._store_headers)):
                        details.append(
                            getattr(store, self._store_headers[i].lower()))
                    line = ';'.join(details)
                    file.write(line+'\n')

    def __load_product_data(self):
        with open(self._product_data) as file:
            self._product_headers = file.readline().strip().split(';')
            result = {header: [] for header in self._product_headers}
            count = 0
            for line in file:
                line = line.strip().split(';')
                count += 1
                for k, v in zip(self._product_headers, line):
                    result[k].append(v)
            return result, count

    def create_poducts(self):
        product_dict, count = self.__load_product_data()
        products = []
        for i in range(count):
            dict = {header.lower(): product_dict[header][i]
                    for header in self._product_headers}
            products.append(Product(**dict))
        return products

    def save_product_data(self, products, product_data=None):
        if product_data == None:
            with open(self._product_data, 'w') as file:
                file.write(';'.join(self._product_headers)+'\n')
                for product in products:
                    details = []
                    for i in range(len(self._product_headers)):
                        details.append(
                            getattr(product, self._product_headers[i].lower()))
                    line = ';'.join(details)
                    file.write(line+'\n')
        else:
            with open(product_data, 'w') as file:
                file.write(';'.join(self._product_headers)+'\n')
                for product in products:
                    details = []
                    for i in range(len(self._product_headers)):
                        details.append(
                            getattr(product, self._product_headers[i].lower()))
                    line = ';'.join(details)
                    file.write(line+'\n')
