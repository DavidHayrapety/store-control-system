from .db import DataBase
from .store import Store
from .product import Product


class Controller:

    def __init__(self, archive):
        self.db = DataBase(archive)
        self.stores = self.db.create_stores()

    def sync(self):
        self.db.save_data(self.stores,"example.csv")

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
                    print(target.__str__)
                case "DELETE":
                    match target_type.__name__:
                        case Store.__name__:
                            self.delete_store(target)
                        case Product.__name__:
                            pass  # TODO
                case "UPDATE":
                    match target_type.__name__:
                        case Store.__name__:
                            ask=input("Do you want to uppdate information of a store or a product in it [info, product]: ")
                            match ask.lower():
                                case 'info':
                                    self.update_store(target, target_type)
                                case 'product':
                                    ask=input("Do you want to remove or add product [remove, add]: ")
                                    match ask:
                                        case 'remove':
                                            self.remove_product_from_store(target)
                                        case 'add':
                                            self.add_product_to_store(target)
                        case Product.__name__:
                            pass # TODO
        else:
            if target_type.__name__ == Store.__name__:
                self.create_store()
            elif target_type.__name__ == Product.__name__:
                self.create_product()
        self.sync()

    def create_store(self):
        address = input('Enter the address of the store: ')
        while True:
            capacity = input('Enter the capacity of the store: ')
            if capacity.isdigit() and int(capacity) > 0:
                break
        self.stores.append(Store(address, capacity))

    def update_store(self, store, store_class):
        if not store_class.get_by_id(store.id):
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
        for i, el in enumerate(self.stores):
            if el.id == store.id:
                del self.stores[i]

    def create_product(self):
        name = input('Enter the name of the product: ')
        category = input('Enter the category of the product: ')
        while True:
            price = input('Enter the price of the product: ')
            if price.isdigit() and price > 0:
                break
        Product(name,price,category)

    def add_product_to_store(self, store):
        product_id=input("ENter the ID of the product you want to add: ")
        quantity=input("Now, enter the quantity of the product you want to add: ")
        store.add_product(product_id,quantity)

    def remove_product_from_store(self, store):
        product_id=input("ENter the ID of the product you want to add: ")
        ask=input("Do you want to remove the product completely [Yes,No]: ")
        if ask.lower()=='no':
            quantity=input("Now, enter the quantity of the product you want to remove: ")
            store.remove_product(product_id,quantity)
        else:
            store.remove_product(product_id,quantity=None)
