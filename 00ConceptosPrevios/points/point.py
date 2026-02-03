import math


class Point:
    def __init__(self, x: float, y: float):
        self.__x: float = x
        self.__y: float = y

    def modulo(self) -> float:
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @x.setter
    def x(self, x: float) -> None:
        self.__x = x

    @y.setter
    def y(self, y: float) -> None:
        self.__y = y

    def __eq__(self, other) -> bool:
        return self.__x == other.__x and self.__y == other.__y

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"
