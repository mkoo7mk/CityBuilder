import Classes.Parrents.MapFile as CMap
from Classes.Parrents.BuildingFile import Building
from Classes.Buildings.CommercialBuildingFile import CommercialBuilding
from Classes.Buildings.IndustrialBuildingFile import IndustrialBuilding
from Classes.Buildings.ResidenceHouseFile import ResidenceHouse
from Classes.Parrents.RendererFile import main
from Classes.Parrents.MenuBarFile import MenuBar

m = CMap.Map(id=0)
rh = ResidenceHouse("R", 0)
ib = IndustrialBuilding("I", 1)
cb = CommercialBuilding("C", 2)
mb = MenuBar(cb, rh, ib)
main()
