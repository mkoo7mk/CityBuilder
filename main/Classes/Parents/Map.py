from math import sqrt
from random import randint

from .ABSObject import ABSObject
from .AbscissaOfTile import Abscissa
from .Cell import Cell
from ..Terrains.Grass import Grass


class Map(ABSObject):
    def __init__(self, id: int, name=None) -> None:
        super().__init__(name, id)
        if name is None:
            self.__name = "Beverley hills"
        else:
            self.__name = name
        self.__id = id
        self.size = 625  # How many cells will a map have
        s = int(sqrt(self.size))
        self.cells = [[Cell(Grass((0, round(randint(100, 255) / 255, 1), 0), "grass", None, Abscissa(x, y, x + s, y + s))) for x in range(s)] for y in range(s)]

    def print_map(self) -> None:
        for y in range(-len(self.cells), 0):
            print(self.cells[y])
        print()
