from .employee import Employee


class Manager(Employee):
    """
    This class represent a Manager
    """
    def __init__(self, age: int, name: str, nSegsocial: str,
                 salary: float, bonus: float):
        super().__init__(age, name, nSegsocial, salary)
        self.__bonus: float  # creating bonus attribute
        self.bonus = bonus  # using setter property for bonus

    @property
    def bonus(self) -> float:
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus: float) -> None:
        self.__bonus = bonus
