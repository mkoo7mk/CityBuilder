from Classes.Renderer import main
from .Classes.Buildings.CommercialBuilding import CommercialBuilding
from .Classes.Buildings.IndustrialBuilding import IndustrialBuilding
from main.Classes.Buildings.ResidenceHouse import ResidenceHouse
from main.Classes.Map import Map
from main.Classes.MenuBar import MenuBar

m = Map(id=0)
rh = ResidenceHouse("R", 0)
ib = IndustrialBuilding("I", 1)
cb = CommercialBuilding("C", 2)
mb = MenuBar(cb, rh, ib)
main()
