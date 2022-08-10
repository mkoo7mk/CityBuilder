from .ABSObject import ABSObject
from typing import Union

from .Person import Person
from .Vehicle import Vehicle


class Building(ABSObject):
    def __init__(self, name: str, id: int, color: tuple, power_usage: int, power_output: int, water_usage: int, water_output: int,
                 min_people: int, people_capacity: int, max_level: int, is_habitable: int, max_vehicles: int, cost: int, upkeep: int):
        super().__init__(name, id)
        self._color = color
        self.__onFire = False
        self.__isCollapsed = False
        self.__model = None
        self.__level = 1
        self.__cost = cost
        self.__maxLevel = max_level
        self.__isHabitable = is_habitable
        self.__power_usage = power_usage
        self.__power_output = power_output
        self.__water_usage = water_usage
        self.__water_output = water_output
        self.__min_people_needed = min_people
        self.__people_capacity = people_capacity
        self.__peopleIn = []
        self.__vehiclesIn = []
        self.__max_vehicles = max_vehicles

    def get_color(self) -> tuple:
        return self._color

    def get_model(self) -> Union[None]:
        return self.__model

    def get_cost(self) -> int:
        return self.__cost

    def upgrade(self) -> None:
        if self.__level + 1 < self.__maxLevel:
            self.__level += 1
            self.update_stats()

    def update_stats(self) -> None:
        temp1 = 1 - self.__level / 100
        temp2 = 1 + self.__level / 100
        self.__water_usage = round(self.__water_usage * temp1)
        self.__water_output = round(self.__water_output * temp2)
        self.__power_usage = round(self.__power_usage * temp1)
        self.__power_output = round(self.__power_output * temp2)

    def destroy(self):
        pass

    def add_person(self, person: Person) -> None:
        if self.__people_capacity > len(self.__peopleIn):
            self.__peopleIn.append(person)

    def remove_person(self, person: Person) -> None:
        self.__peopleIn.remove(person)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        if self.__max_vehicles > len(self.__vehiclesIn):
            self.__vehiclesIn.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        self.__vehiclesIn.remove(vehicle)

    def get_power_usage(self) -> float:
        return self.__power_usage

    def get_power_output(self) -> float:
        return self.__power_output

    def get_water_usage(self) -> float:
        return self.__water_usage

    def get_water_output(self) -> float:
        return self.__water_output

    def get_level(self) -> float:
        return self.__level

    def get_people_in(self) -> list:
        return self.__peopleIn

    def get_vehicles_in(self) -> list:
        return self.__vehiclesIn
