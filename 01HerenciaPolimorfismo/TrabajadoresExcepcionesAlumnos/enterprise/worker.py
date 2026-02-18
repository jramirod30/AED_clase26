from typing import override
from person.person import Person
from abc import ABC, abstractmethod


class Worker(Person, ABC):
    """
    This class define a worker
    """
    def __init__(self, age: int, name: str, nSegSocial: str):
        super().__init__(age, name)
        self.__nSegSocial = nSegSocial

    @abstractmethod
    def monthly_payment(self) -> float:
        pass

    @override
    def __str__(self) -> str:
        return f"{super().__str__()} nSegSocial: {self.nSegSocial}"

    @property
    def nSegSocial(self) -> str:
        return self.__nSegSocial
