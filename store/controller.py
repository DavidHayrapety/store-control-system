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
            match action:
                case "GET":
                    return target
                case "DELETE":
                    match target_type.__name__:
                        case Store.__name__:
                            self.delete_store(target)
                        case Product.__name__:
                            pass # TODO
                case "UPDATE":
                    match target_type.__name__:
                        case Store.__name__:
                            self.update_store(target)
                        case Product.__name__:
                            pass# TODO
        else:
            if target_type.__name__ == Store.__name__:
                self.create_store()
            elif target_type.__name__ == Product.__name__:
                self.create_product()
        # TODO: do not implement syncronising
        self.sync()

    def get_store(self):
        id = input("Enter the id of the store you want to get: ")
        for i in self.stores:
            if i.id == id:
                return i

    def create_store(self):
        address = input('Enter the address of the store: ')
        while True:
            capacity = input('Enter the capacity of the store: ')
            if capacity.isdigit():
                capacity = int(capacity)
                break
        Store(address, capacity)

    def update_store(self, store):
        # id = input("Enter the id of the store you want to update: ")
        if not self.get_store(store.id):
            return
        while True:
            change = input(
                'Enter the info which you want to update [address, capacity]: ').upper()
            if change in ("ADDRESS", "CAPACITY"):
                if change == 'ADDRESS':
                    store.address = input(
                        "Enter a new address for the store: ")
                else:
                    while True:
                        capacity = input('Enter a new capacity of the store: ')
                        if capacity.isdigit():
                            store.capacity = int(capacity)
                            break
                break

    def delete_store(self, store):
        # id = input("Enter the id of the store you want to delete: ")
        for i, el in enumerate(self.stores):
            if el.id == store.id:
                del self.stores[i]

    def get_product(self):
        pass

    def create_product(self):
        pass

    def add_product_to_store(self):
        pass
