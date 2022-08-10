from random import randint
from typing import Union

from .Building import Building
from .Map import Map
from .MenuBar import MenuBar
from .Road import Road
from ..Buildings.CommercialBuilding import CommercialBuilding
from ..Buildings.IndustrialBuilding import IndustrialBuilding
from ..Buildings.ResidenceHouse import ResidenceHouse
from ..ConstructBuildings.ServiceBuildings import FireHouse


class MouseHandler(object):
    def clicked(self, x: int, y: int, m: Map, menu: MenuBar) -> int:
        building = m.cells[x][y].get_building()
        if building is None:
            b = self.build(menu.selected)
            m.cells[x][y].set_building(b)
            return b.get_cost()
        else:
            building.print_name()
            return 0

    def build(self, selected: int) -> Union[Building, Road]:
        print(selected)
        if selected == 1:
            return ResidenceHouse(self.get_building_name(selected), 0)
        elif selected == 2:
            return IndustrialBuilding(self.get_building_name(selected), 0)
        elif selected == 3:
            return CommercialBuilding(self.get_building_name(selected), 0)
        elif selected == 0:
            return Road(self.get_building_name(selected), 0)
        elif selected == 5:
            a = FireHouse
            return a

    @staticmethod
    def get_building_name(type_of_building: int) -> str:
        if type_of_building == 0:
            with open(
                    "C:\\Users\\marti\\Desktop\\Programovanie\\Python games\\CityBuilder\\main\\Assets\\Constants\\StreetNames.txt",
                    "r") as file:
                f = file.readlines()
                out = f[randint(0, len(f))].replace("\n", "")
                file.close()

        elif type_of_building == 1:
            with open(
                    "C:\\Users\\marti\\Desktop\\Programovanie\\Python games\\CityBuilder\\main\\Assets\\Constants\\ResidentialBuildingNames.txt",
                    "r") as file:
                f = file.readlines()
                out = f[randint(0, len(f))].replace("\n", "")
                file.close()
        elif type_of_building == 2:
            with open(
                    "C:\\Users\\marti\\Desktop\\Programovanie\\Python games\\CityBuilder\\main\\Assets\\Constants\\ResidentialBuildingNames.txt",
                    "r") as file:
                f = file.readlines()
                out = f[randint(0, len(f))].replace("\n", "")
                file.close()
        elif type_of_building == 3:
            with open(
                    "C:\\Users\\marti\\Desktop\\Programovanie\\Python games\\CityBuilder\\main\\Assets\\Constants\\CommercialBuildingNames.txt",
                    "r") as file:
                f = file.readlines()
                out = f[randint(0, len(f))].replace("\n", "")
                file.close()

        return out
