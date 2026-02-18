from typing import override
from .worker import Worker


class Employee(Worker):
    """
    this class represent an enterprise Worker
    """

    def __init__(self, age: int, name: str, nSegSocial: str, salary: float):
        """
        Constructor for employee
        **PRE:** age >=0 and salary >=0
        :param age: age of the employee. It must be > = 0
        :param name: employees' name
        :param nSegSocial: ID for seguridad social
        :param salary: the yearly payment for this worker.  It must be >= 0
        """
        super().__init__(age, name, nSegSocial)
        self.__salary: float
        # salary is the yearly payment for this worker
        self.salary = salary

    @override
    def monthly_payment(self) -> float:
        return self.salary / 14

    @override
    def __str__(self) -> str:
        return f"{super().__str__()} salary: {self.salary}"

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        """
        Set the salary for this employee
        **PRE:** salary >= 0
        """
        self.__salary = salary
