from ..Parents.Building import Building


class IndustrialBuilding(Building):
    def __init__(self, name, id):
        super().__init__(name=name, id=id, color=(200, 20, 0), power_usage=30, power_output=0, water_output=0, water_usage=35, pollution=40, noise_pollution=30, max_level=10, max_vehicles=3, cost=1500, min_people=5, people_capacity=40, is_habitable=False, upkeep=200)
