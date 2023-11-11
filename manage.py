from sys import argv
from store import Controller

store_archive = argv[1]
product_archive = argv[2]

ctrl = Controller(store_archive,product_archive)

while True:
    ctrl.get_command()
