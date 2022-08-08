from main.Classes.Parrents.Entity import Entity


class Person(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.gender = True
