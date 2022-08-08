import Classes.Parents.Map as CMap
from Classes.Buildings.CommercialBuildingFile import CommercialBuilding
from Classes.Buildings.IndustrialBuildingFile import IndustrialBuilding
from Classes.Buildings.ResidenceHouseFile import ResidenceHouse
from Classes.Parents.Renderer import main
from Classes.Parents.MenuBar import MenuBar

m = CMap.Map(id=0)
rh = ResidenceHouse("R", 0)
ib = IndustrialBuilding("I", 1)
cb = CommercialBuilding("C", 2)
mb = MenuBar(cb, rh, ib)
main()
