from typing import override

from figures import IFigure


class Photo(IFigure):

    def __init__(self, side1: float, side2: float):
        self.__side1 = side1
        self.__side2 = side2

    @override
    def area(self) -> float:
        return self.__side1 * self.__side2

    @override
    def perimeter(self) -> float:
        return 2 * (self.__side1 + self.__side2)
