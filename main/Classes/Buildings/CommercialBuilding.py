from ..Parents.Building import Building


class CommercialBuilding(Building):
    def __init__(self, name, id):
        super().__init__(name, id)
        self._color = (52, 180, 235)