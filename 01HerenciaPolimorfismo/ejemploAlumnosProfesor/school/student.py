from abc import ABC, abstractmethod
from typing import override
from person import Person


class Student(ABC, Person):
    def __init__(self, name: str, age: int, class_num: int, academic_level: str):
        super().__init__(name, age)
        self.__class_num: int = class_num  # higher school year
        self.__academic_level = academic_level

    @abstractmethod
    def get_subjects(self) -> str:
        pass

    @abstractmethod
    def monthly_rate(self) -> float:
        pass

    @override
    def __str__(self):
        return f"{Person.__str__(self)}, monthly payment: {self.monthly_rate()} "

    #  properties definition
    @property
    def class_num(self) -> int:
        return self.__class_num

    @class_num.setter
    def class_num(self, class_num: int) -> None:
        self.__class_num = class_num

    @property
    def academic_level(self) -> str:
        return self.__academic_level

    @academic_level.setter
    def academic_level(self, academic_level: str):
        self.__academic_level = academic_level
