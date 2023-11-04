from uuid import uuid4


class Store:

    _instances = []

    def __init__(self, address, capacity, id=None):
        self._address = address
        self._capacity = capacity
        self._products = {}
        if id is None:
            id = uuid4()
        self._id = id
        Store._instances.append(self)

    @property
    def free_quantity(self):
        used_quantity = sum(self._products.values())
        return self._capacity - used_quantity
    
    @property
    def instances(self):
        return self._instances
    
    @property
    def address(self):
        return self._address
    
    @property
    def capacity(self):
        return self._capacity

    @property
    def id(self):
        return self._id
    
    def add_product(self, product, quantity=1):
        if self.free_quantity < quantity:
            return False
        current_quatity = self._products.get(product, 0)
        self._products[product] = current_quatity + quantity
        return True

    def remove_product(self, product, quantity=None):
        if not self._products.get(product):
            return False
        if quantity is None:
            quantity = self._products[product]
        self._products[product] -= quantity
        return True

    @classmethod
    def get_by_id(cls, id):
        for store in cls._instances:
            if store._id == id:
                return store

    @property
    def __str__(self):
        return (     
            f"Address: {self._address}\n"
            f"Capacity: {self._capacity}\n"
            f"ID: {self._id}\n"
            )
