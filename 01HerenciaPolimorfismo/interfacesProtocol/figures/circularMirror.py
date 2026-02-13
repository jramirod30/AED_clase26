from typing import override

#from .figure import IFigure
import math


class CircularMirror:

    def __init__(self, radius: float):
        self.__radius = radius

    # def perimeter(self) -> float:
    #     return 2 * math.pi * self.__radius

    def area(self) -> float:
        return math.pi * pow(self.__radius, 2)
