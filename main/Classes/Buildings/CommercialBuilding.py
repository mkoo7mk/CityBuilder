from ..Parents.Building import Building


class CommercialBuilding(Building):
    def __init__(self, name, id):
        super().__init__(name, id, (.1, .2, .8))
