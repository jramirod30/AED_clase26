from .worker import Worker


class OutsideConsultant (Worker):
    """
    This class represent an Outside Consultant
    """
    def __init__(self, age: int, name: str, nSegSocial: str, rate: float, hours: float, company: str):
        super().__init__(age, name, nSegSocial)
        self.__company: str = company
        self.__rate: float
        self.__hours: float
        self.rate = rate
        self.hours = hours

    @property
    def company(self) -> str:
        return self.__company

    @property
    def hours(self) -> float:
        return self.__hours

    @property
    def rate(self) -> float:
        return self.__rate

    @company.setter
    def company(self, company: str) -> None:
        self.__company = company

    @hours.setter
    def hours(self, hours: float) -> None:
        self.__hours = hours

    @rate.setter
    def rate(self, rate) -> None:
        self.__rate = rate
