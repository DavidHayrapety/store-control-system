from sys import argv
from store import Controller

archive = argv[1]

ctrl = Controller(archive)

while True:
    ctrl.get_command()
