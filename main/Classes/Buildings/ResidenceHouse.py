from ..Parents.Building import Building


class ResidenceHouse(Building):
    def __init__(self, name, id):
        super().__init__(name, id)
        self._color = (49, 133, 71)