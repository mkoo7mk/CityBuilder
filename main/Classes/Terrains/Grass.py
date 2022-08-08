from ..Parents.AbscissaOfTile import Abscissa
from ..Parents.Terrain import Terrain


class Grass(Terrain):
    def __init__(self, color: tuple, type: str, resource: None, start_point: Abscissa):
        super().__init__(color, type, resource, start_point)

    def __str__(self):
        return self.start_point.x0

    def __repr__(self):
        return str(self.start_point.x0)
