from random import randint
from typing import Union

from .Building import Building
from .Game import Game
from .Road import Road
from ..Buildings.CommercialBuilding import CommercialBuilding
from ..Buildings.IndustrialBuilding import IndustrialBuilding
from ..Buildings.ResidenceHouse import ResidenceHouse
from ..ConstructBuildings.ServiceBuildings import FireHouse, PoliceStation, MedicalClinic


class MouseHandler(object):
    def clicked(self, x: int, y: int, g: Game):
        building = g.map.cells[x][y].get_building()
        if building is None:
            b = self.build(g.menu_bar.selected)
            if b is not None:
                if g.get_money() - b.get_cost() >= 0:
                    g.pay(b.get_cost())
                    g.map.cells[x][y].set_building(b)
                else:
                    print("Not enough money! ")
        else:
            if g.menu_bar.selected == 9:
                g.map.cells[x][y].destroy()
                g.get_paid(round(building.get_cost() / 2))
            else:
                building.print_name()

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
            temp = FireHouse
            return temp
        elif selected == 4:
            temp = MedicalClinic
            return temp
        elif selected == 6:
            temp = PoliceStation
            return temp

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
                out = f[randint(0, len(f) - 1)].replace("\n", "")
                file.close()
        elif type_of_building == 2:
            with open(
                    "C:\\Users\\marti\\Desktop\\Programovanie\\Python games\\CityBuilder\\main\\Assets\\Constants\\ResidentialBuildingNames.txt",
                    "r") as file:
                f = file.readlines()
                out = f[randint(0, len(f)) - 1].replace("\n", "")
                file.close()
        elif type_of_building == 3:
            with open(
                    "C:\\Users\\marti\\Desktop\\Programovanie\\Python games\\CityBuilder\\main\\Assets\\Constants\\CommercialBuildingNames.txt",
                    "r") as file:
                f = file.readlines()
                out = f[randint(0, len(f) - 1)].replace("\n", "")
                file.close()

        return out
