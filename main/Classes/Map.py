from ABSObject import ABSObject


class Map(ABSObject):
    def __init__(self, id: int, name=None) -> None:
        super().__init__(name, id)
        if name is None:
            self.__name = "Beverley hills"
        else:
            self.__name = name
        self.__id = id
        self.size = 500  # How many cells will a map have
