from ..Parents.Building import Building
from ..Parents.Person import Person


class MedicalClinic(Building):
    def __init__(self, name: str, id: int, color: tuple, power_usage: int, power_output: int, water_usage: int,
                 water_output: int, min_people: int, people_capacity: int, max_level: int, is_habitable: bool,
                 max_vehicles: int, cost: int, upkeep: int, pollution: int, noise_pollution: int):
        super().__init__(name, id, color, power_usage, power_output, water_usage, water_output, min_people,
                         people_capacity, max_level, is_habitable, max_vehicles, cost, upkeep, pollution,
                         noise_pollution)
        self.__patient_capacity = 50
        self.__patients = []

    def get_patients(self) -> list:
        return self.__patients

    def add_patient(self, patient: Person) -> None:
        if self.__patient_capacity >= len(self.__patients):
            self.__patients.append(patient)
    
    def remove_patient(self, patient: Person):
        try:
            self.__patients.remove(patient)
        except ValueError as e:
            return e