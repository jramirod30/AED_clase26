from typing import override

from .employee import Employee


class Manager(Employee):
    """
    This class represent a Manager
    """
    def __init__(self, age: int, name: str, nSegSocial: str,
                 salary: float, bonus: float):
        """
        Constructor for Manager
        **PRE:** age >=0 and salary >=0 and bonus >=0
        :param age: age of the employee. It must be > = 0
        :param name: employees' name
        :param nSegSocial: ID for seguridad social
        :param salary: the yearly payment for this worker. It must be >= 0
        :param bonus: bonus for manager. It must be >= 0
        """
        super().__init__(age, name, nSegSocial, salary)
        self.__bonus: float  # creating bonus attribute
        self.bonus = bonus  # using setter property for bonus

    @override
    def __str__(self) -> str:
        return f"{super().__str__()} bonus: {self.bonus}"

    @override
    def monthly_payment(self) -> float:
        return super().monthly_payment() + self.bonus

    @property
    def bonus(self) -> float:
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus: float):
        """
        Set the bonus
        **PRE:** bonus >= 0
        :param bonus: bonus for manager.
        """
        self.__bonus = bonus
