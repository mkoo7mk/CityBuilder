from main.Classes.Parents.ABSObject import ABSObject


class Road(ABSObject):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.__color = (.1, .1, .1)
        self.__length = 0
        self.__type = 0
        self.__level = 0
        self.__cost = 50

    def get_color(self) -> tuple:
        return self.__color

    def get_cost(self) -> int:
        return self.__cost