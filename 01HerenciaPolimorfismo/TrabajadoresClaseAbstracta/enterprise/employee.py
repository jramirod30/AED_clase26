import sys
from typing import Final, override

from .worker import Worker


class Employee(Worker):
    """
    this class represent an enterprise Worker
    """
    SMI:Final[float] = 12000

    def __init__(self, age: int, name: str, nSegSocial: str, salary: float):
        """
        Constructor for employee
        **PRE:** age >=0 and salary >= SMI
        :param age: age of the employee. It must be > = 0
        :param name: employees' name
        :param nSegSocial: ID for seguridad social
        :param salary: the yearly payment for this worker.  It must be >= SMI
        """
        super().__init__(age, name, nSegSocial)
        # salary es el sueldo anual
        self.__salary: float # creating salary attribute
        self.salary = salary # using setter property for salary

    def __str__(self):
        return f"{super().__str__()} con un salario anual: {self.salary}"


    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        """
        Set the yearly salary for this employee
        **PRE:** salary >= SMI
        """
        if salary < Employee.SMI:
           print("Salario debe ser >= SMI",file=sys.stderr)
           return
        self.__salary = salary

    def __str__(self) -> str:
        return f"{super().__str__()} yearly salary: {self.salary}"

    @override
    def monthly_payment(self) -> float:
        return self.salary / 14