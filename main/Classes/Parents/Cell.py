from typing import Union

from .Building import Building
from .Road import Road
from .Terrain import Terrain


class Cell:
    def __init__(self, terrain: Terrain):
        self.__terrain = terrain
        self.__building = None
        self.__road = None
        # May add air stuff later

    def get_road(self) -> Union[None, Road]:
        return self.__road

    def get_terrain(self) -> Terrain:
        return self.__terrain

    def get_building(self) -> Union[None, Building]:
        return self.__building

    def set_building(self, building) -> None:
        self.__building = building

