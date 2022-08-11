from ..Parents.Building import Building


class CommercialBuilding(Building):
    def __init__(self, name, id):
        # TODO make a class from this please asap
        super().__init__(name=name, id=id, color=(.1, .2, .8), upkeep=150, is_habitable=False, people_capacity=50, min_people=3, max_level=20, max_vehicles=10, noise_pollution=10, pollution=0, cost=1000, water_usage=10, power_usage=10, water_output=0, power_output=0)
