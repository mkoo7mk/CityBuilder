from ..Parents.Building import Building


class ResidenceHouse(Building):
    def __init__(self, name, id):
        super().__init__(name=name, id=id, color=(0.5, .99, .2), min_people=0, people_capacity=20, is_habitable=True, upkeep=100, max_level=15, max_vehicles=5, pollution=0, noise_pollution=0, water_usage=5, water_output=0, power_output=0, power_usage=5, cost=1000)
