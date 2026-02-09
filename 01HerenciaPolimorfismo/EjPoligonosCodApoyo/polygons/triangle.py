from typing import override

from polygons import Polygon, PointList


class Triangle(Polygon):

    # The constructor does not verify that points define a triangle
    def __init__(self, points: PointList):
        """
        PRE: len(points) == 3
        POST: inicialice triangle vertex
        """
        pass

    @override
    def get_type(self) -> str:
        """
        POST: classify triangle as equilateral, isosceles or scalene
        """
        pass
