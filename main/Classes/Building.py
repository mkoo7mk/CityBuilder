from ABSObject import ABSObject


class Building(ABSObject):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)

    def build(self):
        pass

    def destroy(self):
        pass