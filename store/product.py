class Product:

    _instances = []

    def __init__(self, name, price, category, id=None):
        self.name = name
        self.__price = price
        self.category = category
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
        pass
