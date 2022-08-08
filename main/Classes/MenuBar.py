from Buildings.IndustrialBuilding import IndustrialBuilding
from Buildings.CommercialBuilding import CommercialBuilding
from Buildings.ResidenceHouse import ResidenceHouse


class MenuBar(object):
    def __init__(self, cb: CommercialBuilding, rh: ResidenceHouse, ib: IndustrialBuilding):
        self.selected = 0
        self.buildings = [rh, ib, cb]
        self.maxLength = len(self.buildings) - 1
