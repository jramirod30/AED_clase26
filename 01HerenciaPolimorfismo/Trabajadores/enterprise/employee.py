from .worker import Worker

class Employee(Worker):
    """
    this class represent an enterprise Worker
    """
    def __init__(self, age: int, name: str, nSegSocial: str, salary: float):
        super().__init__(age, name, nSegSocial)
        self.__salary: float
        self.salary = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        self.__salary = salary
