# from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

@runtime_checkable
class IFigure(Protocol):

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass
