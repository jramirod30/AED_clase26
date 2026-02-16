from abc import abstractmethod, ABC

from person.person import Person

class Worker(Person, ABC):
    """
    This class define a worker
    """

    def __init__(self, age: int, name: str, nSegSocial: str):
        super().__init__(age, name)
        self.__nSegSocial = nSegSocial

    def __str__(self):
        return (f"{super().__str__()} "
                f" número de seguridad social: {self.nSegSocial}")


    @property
    def nSegSocial(self) -> str:
        return self.__nSegSocial

    @abstractmethod
    def monthly_payment(self) -> float:
        pass