class Entity(object):
    def __init__(self, name):
        self.__name = name
        self.__age = 10.0

    def get_name(self) -> str:
        return self.__name

    def change_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_age(self) -> float:
        return self.__age

    def change_age(self, new_age: float):
        self.__age = new_age

    def increase_age(self):
        self.__age += 0.01
