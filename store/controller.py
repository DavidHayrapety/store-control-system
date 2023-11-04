from .db import DataBase
from .store import Store
from .product import Product


class Controller:

    def __init__(self, archive):
        self.db = DataBase(archive)
        self.stores = self.db.create_stores()

    def sync(self):
        self.db.save_data(self.stores)

    def __get_action(self):
        while True:
            command = input(
                "Enter action type [create, get, update, delete]: ").upper()
            if command in ('CREATE', 'GET', 'UPDATE', 'DELETE'):
                return command

    def __get_target_type(self):
        target_types = {
            'STORE': Store,
            'PRODUCT': Product
        }
        while True:
            target_type = input("Enter target type [store, product]: ").upper()
            if target_type in target_types.keys():
                break
        return target_types[target_type]

    def __get_target(self, target_cls):
        while True:
            target_id = input("Enter target id: ")
            target = target_cls.get_by_id(target_id)
            if target:
                return target
            print(f'{target_cls.__name__} with id "{target_id}" not found')

    def get_command(self):
        action = self.__get_action()
        target_type = self.__get_target_type()
        if action != 'CREATE':
            target = self.__get_target(target_type)
        else:
            if target_type == 'STORE':
                self.create_store()
            elif target_type == 'PRODUCT':
                self.create_product()
        self.sync()

    def get_store(self, id):
        for i in Store._instances:
            if i._id == id:
                return i
        return False

    def create_store(self):
        address = input('Enter the address of the store: ')
        while True:
            capacity = input('Enter the capacity of the store: ')
            if capacity.isdigit():
                capacity = int(capacity)
                break
        Store(address, capacity)

    def update_store(self, id):
        if not self.get_store(id):
            return False
        while True:
            change = input(
                'Enter the info which you want to update [address, capacity]: ').upper()
            if change in ("ADDRESS", "CAPACITY"):
                store = self.get_store(id)
                if change == 'ADDRESS':
                    store._address = input(
                        "Enter a new address for the store: ")
                else:
                    while True:
                        capacity = input('Enter a new capacity of the store: ')
                        if capacity.isdigit():
                            store._capacity = int(capacity)
                            break
                break

    def delete_store(self, id):
        for i, el in enumerate(Store._instances):
            if el._id == id:
                del Store._instances[i]
        return False

    def get_product(self):
        pass

    def create_product(self):
        pass

    def add_product_to_store(self):
        pass
