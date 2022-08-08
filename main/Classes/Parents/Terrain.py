from .AbscissaOfTile import Abscissa


class Terrain(object):

    def __init__(self, color: tuple, type: str, resource: None, start_point: Abscissa):
        self.color = color
        self.type = type
        self.resource = resource
        self.start_point = start_point

    def __on_click(self):
        pass
