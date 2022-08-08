from .ABSObject import ABSObject


class Building(ABSObject):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.color = (40, 40, 150)
        self.model = None
        self.level = 0
        self.maxLevel = 5
        self.isHabitable = False
        self.peopleIn = []

    def build(self):
        pass

    def upgrade(self):
        pass

    def destroy(self):
        pass
