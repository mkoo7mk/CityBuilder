# Save/open handling
# Will have map and list of cells
from .Map import Map
from .MenuBar import MenuBar


class Game(object):
    def __init__(self, m: Map, mb: MenuBar):
        self.map = m
        self.menu_bar = mb

    def save_game(self):
        pass

    def load_game(self):
        pass
