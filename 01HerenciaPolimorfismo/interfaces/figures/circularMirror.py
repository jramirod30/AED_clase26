from typing import override

from figures import IFigure
import math


class CircularMirror(IFigure):

    def __init__(self, radius: float):
        self.__radius = radius

    @override
    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    @override
    def area(self) -> float:
        return math.pi * pow(self.__radius, 2)
