from ..Parents.Building import Building
from ..Parents.Person import Person


class Police(Building):
    def __init__(self, name: str, id: int, color: tuple, power_usage: int, power_output: int, water_usage: int,
                 water_output: int, min_people: int, people_capacity: int, max_level: int, is_habitable: bool,
                 max_vehicles: int, cost: int, upkeep: int, pollution: int, noise_pollution: int):
        super().__init__(name, id, color, power_usage, power_output, water_usage, water_output, min_people,
                         people_capacity, max_level, is_habitable, max_vehicles, cost, upkeep, pollution,
                         noise_pollution)
        self.__prison_capacity = 10
        self.__prisoners = []

    def get_prisoners(self) -> list:
        return self.__prisoners

    def add_prisoner(self, prisoner: Person) -> None:
        if self.__prison_capacity > len(self.__prisoners):
            self.__prisoners.append(prisoner)

    def remove_prisoner(self, prisoner: Person):
        try:
            self.__prisoners.remove(prisoner)
        except ValueError as e:
            return e
