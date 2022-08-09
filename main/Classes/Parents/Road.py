from main.Classes.Parents.ABSObject import ABSObject


class Road(ABSObject):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.length = 0
        self.type = 0
        self.level = 0