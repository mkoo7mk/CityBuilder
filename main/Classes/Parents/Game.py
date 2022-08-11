# Save/open handling
from .Map import Map
from .MenuBar import MenuBar


class Game(object):
    def __init__(self, m: Map, mb: MenuBar):
        self.map = m
        self.menu_bar = mb
        self.__money = 50000

    def pay(self, amount: int):
        self.__money -= amount
        print(self.__money)

    def get_paid(self, amount: int):
        self.__money += amount

    def save_game(self):
        pass

    def load_game(self):
        pass
