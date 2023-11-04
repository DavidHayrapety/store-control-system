from store import Store


class DataBase:

    _headers = []

    def __init__(self, filename):
        self._filename = filename

    def __load_data(self):
        with open(self._filename) as file:
            self._headers = file.readline().strip().split(';')
            result = {header: [] for header in self._headers}
            count = 0
            for line in file:
                line = line.strip().split(';')
                count += 1
                for k, v in zip(self._headers, line):
                    result[k].append(v)
            return result, count

    def create_stores(self):
        store_dict, count = self.__load_data()
        stores = []
        for i in range(count):
            dict={header.lower():store_dict[header][i] for header in self._headers}
            stores.append(Store(**dict))
        return stores

    def save_data(self, stores, filename=None):
        if filename==None:
            with open(self._filename) as file:
                for store in stores:
                    details = [getattr(store,h) for h in self._headers]
                    line=';'.join(details)
                    file.writelines(line)
        else:
            with open(filename, 'w') as file:
                file.write(';'.join(self._headers)+'\n')
                for store in stores:
                    details=[]
                    for i in range(len(stores)):
                        details.append(getattr(store,f'_{self._headers[i].lower()}'))
                    line=';'.join(details)
                    file.write(line+'\n')
