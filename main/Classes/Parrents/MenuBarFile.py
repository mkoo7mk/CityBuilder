from ..Buildings.ResidenceHouseFile import ResidenceHouse
from ..Buildings.IndustrialBuildingFile import IndustrialBuilding
from ..Buildings.CommercialBuildingFile import CommercialBuilding


class MenuBar(object):
    def __init__(self, cb, rh, ib):
        self.selected = 0
        self.buildings = [rh, ib, cb]
        self.maxLength = len(self.buildings) - 1
