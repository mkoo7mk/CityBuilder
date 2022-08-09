from .ABSObject import ABSObject
from typing import Union


class Building(ABSObject):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self._color = (40, 40, 150)
        self.__model = None
        self.__level = 0
        self.__maxLevel = 5
        self.__isHabitable = False
        self.__peopleIn = []

    def get_color(self) -> tuple:
        return self._color

    def get_model(self) -> Union[None]:
        return self.__model

    def build(self):
        pass

    def upgrade(self):
        pass

    def destroy(self):
        pass
