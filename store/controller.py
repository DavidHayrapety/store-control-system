from .db import DataBase
from .store import Store
from .product import Product

class Controller:

    def __init__(self, archive):
        self.db = DataBase(archive)
        self.stores = self.db.load_data()
        

    def sync(self):
        self.db.save_data(self.stores)

    def __get_action(self):
        while True:
            command = input("Enter action type [create, get, update, delete]: ").upper()
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

    def get_store(self):
        pass

    def create_store(self):
        pass

    def update_store(self):
        pass

    def delete_store(self):
        pass

    def get_product(self):
        pass

    def create_product(self):
        pass

    def add_product_to_store(self):
        pass
