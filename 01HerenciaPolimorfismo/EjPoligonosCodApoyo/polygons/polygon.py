from polygons.point import Point
# in python if you need define an abstract class
# must be inherited from ABC and you must use
# abstractmethod decorator for abstract methods
from abc import ABC, abstractmethod

# Defining a type aliases. 'type' is supported by python 3.12 or higher
type PointList = list[Point]


class Polygon(ABC):
    def __init__(self, points: PointList):
        self.__points: PointList = points.copy()  # <-Return a shallow copy of the list
        # self.__size: int = len(points) # <- Redundante se tiene la longitud de la lista
    
	
    def perimeter(self) -> float:
        """
        POST: return polygon perimeter
        """
        pass

    def get_side(self, side: int) -> float:
        """
        PRE: 1 <= side <= size
        POST: return length side
        """
        size: int = len(self.__points)  # Por claridad se define una variable local
        if side < 1 or side > size:
            raise ValueError(f"Side {side} doesn't exist")
        return self.__points[side-1].distance(self.__points[side % size])

    @abstractmethod
    def get_type(self) -> str:
        pass
