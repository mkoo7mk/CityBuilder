from ..Parents.Building import Building
from .Police import Police
from .MedicalClinic import MedicalClinic


FireHouse = Building(name="Fire House", id=0, color=(1, 0, 0), power_usage=20, power_output=0, water_output=0, water_usage=40, max_level=10, max_vehicles=5, min_people=10, people_capacity=30, is_habitable=False, cost=20000, upkeep=500, pollution=0, noise_pollution=10)
MedClinic = MedicalClinic(name="Medical Clinic", id=0, color=(1, 0, .5), power_usage=40, power_output=0, water_output=0, water_usage=30, max_level=10, max_vehicles=5, min_people=5, people_capacity=20, is_habitable=False, cost=20000, upkeep=650, pollution=0, noise_pollution=15)
PoliceStation = Police(name="Police", id=0, color=(0, .2, 1), power_usage=20, power_output=0, water_output=0, water_usage=20, max_level=10, max_vehicles=5, pollution=0, noise_pollution=0, min_people=5, people_capacity=15, is_habitable=False, cost=25000, upkeep=400)
WaterTower = Building(name="Water Tower", id=0, color=(0, .3, .6), power_usage=100, power_output=0, water_output=500, water_usage=0, max_level=1, max_vehicles=0, pollution=0, noise_poution=50, min_people=1, people_capacity=3, is_habitable=False, cost=1000, upkeep=300)
BigWaterTower = Building(name="Big Water Tower", id=0, color=(0.25, .3, .6), power_usage=200, power_output=0, water_output=5000, water_usage=0, max_level=3, max_vehicles=0, pollution=0, noise_poution=65, min_people=3, people_capacity=5, is_habitable=False, cost=5000, upkeep=500)
MasiveWaterTower = Building(name="Masive Water Tower", id=0, color=(0.5, .3, .6), power_usage=1000, power_output=0, water_output=50000, water_usage=0, max_level=1, max_vehicles=0, pollution=0, noise_poution=80, min_people=5, people_capacity=10, is_habitable=False, cost=20000, upkeep=1000)
WindTurbine = Building(name="Wind Turbine", id=0, color=(0, .3, .6), power_usage=0, power_output=100, water_output=0, water_usage=0, max_level=1, max_vehicles=0, pollution=0, noise_poution=60, min_people=0, people_capacity=0, is_habitable=False, cost=1000, upkeep=300)
MediumWindTurbine = Building(name="Medium Wind Turbine", id=0, color=(0, .3, .6), power_usage=0, power_output=1000, water_output=0, water_usage=0, max_level=1, max_vehicles=0, pollution=0, noise_poution=70, min_people=0, people_capacity=0, is_habitable=False, cost=5000, upkeep=400)
EnourmousWindTurbine = Building(name="Enormous Wind Turbine", id=0, color=(0, .3, .6), power_usage=0, power_output=10000, water_output=0, water_usage=0, max_level=1, max_vehicles=0, pollution=0, noise_poution=80, min_people=0, people_capacity=0, is_habitable=False, cost=100000, upkeep=1000)
