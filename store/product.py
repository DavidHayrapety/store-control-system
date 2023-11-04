from uuid import uuid4


class Product:

    _instances = []

    def __init__(self, name, price, category, id=None):
        self.name = name
        self.__price = price
        self.category = category
        if id is None:
            id = uuid4()
        self._id = id
        Product._instances.append(self)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @classmethod
    def get_by_id(cls, id):
        for product in cls._instances:
            if product._id == id:
                return product

    @property
    def info(self):
        return (     
            f"Name: {self.name}\n"
            f"Price: {self.__price}\n"
            f"Category: {self.category}\n"
            f"ID: {self.__id}\n"
            )
