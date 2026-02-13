import sys

from .employee import Employee


class Manager(Employee):
    """
    This class represent a Manager
    """
    def __init__(self, age: int, name: str, nSegSocial: str,
                 salary: float, bonus: float):
        """
        Constructor for Manager
        **PRE:** age >=0 and salary >=SMI and bonus >=0
        :param age: age of the employee. It must be > = 0
        :param name: employees' name
        :param nSegSocial: ID for seguridad social
        :param salary: the yearly payment for this worker. It must be >= SMI
        :param bonus: bonus for manager. It must be >= 0
        """
        super().__init__(age, name, nSegSocial, salary)
        self.__bonus: float  # creating bonus attribute
        self.bonus = bonus  # using setter property for bonus

    def __str__(self) -> str:
        return f"{super().__str__()} bonus: {self.bonus}"

    @property
    def bonus(self) -> float:
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus: float) -> None:
        """
        Set the bonus
        **PRE:** bonus >= 0
        :param bonus: bonus for manager.
        """
        if bonus < 0:
            print(f"bonus must be >= 0 but the bonus given was: {bonus}", file=sys.stderr)
            return
        self.__bonus = bonus
