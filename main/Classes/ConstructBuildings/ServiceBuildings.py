from ..Parents.Building import Building
from .Police import Police


FireHouse = Building(name="Fire House", id=0, color=(1, 0, 0), power_usage=20, power_output=0, water_output=0, water_usage=40, max_level=10, max_vehicles=5, min_people=10, people_capacity=30, is_habitable=False, cost=20000, upkeep=500, pollution=0, noise_pollution=10)
MedicalClinic = Building(name="Medical Clinic", id=0, color=(1, 0, .5), power_usage=40, power_output=0, water_output=0, water_usage=30, max_level=10, max_vehicles=5, min_people=5, people_capacity=20, is_habitable=False, cost=20000, upkeep=650, pollution=0, noise_pollution=15)
PoliceStation = Police(name="Police", id=0, color=(0, .2, 1), power_usage=20, power_output=0, water_output=0, water_usage=20, max_level=10, max_vehicles=5, pollution=0, noise_pollution=0, min_people=5, people_capacity=15, is_habitable=False, cost=25000, upkeep=400)
