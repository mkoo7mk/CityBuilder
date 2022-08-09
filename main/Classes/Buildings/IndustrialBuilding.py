from ..Parents.Building import Building


class IndustrialBuilding(Building):
    def __init__(self, name, id):
        super().__init__(name, id)
        self._color = (200, 20, 0)
