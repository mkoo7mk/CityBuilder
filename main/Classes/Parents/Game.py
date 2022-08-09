# Save/open handling
# Will have map and list of cells
from .Map import Map


class Game(object):
    def __init__(self, m: Map):
        self.map = m

    def save_game(self):
        pass

    def load_game(self):
        pass
