from ..Parents.Building import Building


class ResidenceHouse(Building):
    def __init__(self, name, id):
        super().__init__(name, id, (0.5, .99, .2))
