from MenuBar import MenuBar
from Map import Map


class Game(object):
    def __init__(self, menu: MenuBar, m: Map) -> None:
        self.MAX_BUILDING_TYPES_COUNT = 5
        self.MENU_BAR = menu
        self.MAP = m
        self.save = None
        self.building_list = []
