from sys import argv
from store import Controller

archive = argv[1]

ctl = Controller(archive)

while True:
    ctl.get_command()
