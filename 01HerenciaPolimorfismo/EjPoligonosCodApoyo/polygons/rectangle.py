from typing import override

from polygons import Polygon, PointList


class Rectangle(Polygon):

    # The constructor does not verify that points define a rectangle
    def __init__(self, points: PointList):
        """
        PRE: len(points) == 4
        POST: inicialice rectangle vertex
        """
        if len(points) != 4:
            raise ValueError("Rectangle must be defined by 4 points")
        super().__init__(points)

    @override
    def get_type(self) -> str:
        """
        POST: classify rectangle as square or rectangle
        """
        pass
