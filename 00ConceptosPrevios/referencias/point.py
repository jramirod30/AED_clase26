from __future__ import annotations
import math


class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __copy__(self) -> Point:
        """
        This method is used for copying an instance
        :return:
        """
        # print ("Copying a new point")
        new_point: Point = Point(self.x, self.y)
        return new_point

    def distance(self, other: Point) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.x == other.x and self.y == other.y

    # Properties definition
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float) -> None:
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float) -> None:
        self.__y = y
