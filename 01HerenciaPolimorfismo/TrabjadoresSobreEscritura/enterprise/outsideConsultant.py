import sys

from .worker import Worker


class OutsideConsultant (Worker):
    """
    This class represent an Outside Consultant
    """
    def __init__(self, age: int, name: str, nSegSocial: str,
                 rate: float, hours: float, company: str):
        """
        Constructor for Manager
        **PRE:** age >=0 and rate >=0 and hours >=0
        :param age: age of the employee. It must be > = 0
        :param name: employees' name
        :param nSegSocial: ID for seguridad social
        :param rate: the rate payment per hour. It must be >= 0
        :param hours: working hours for this consultant. It must be >= 0
        """
        super().__init__(age, name, nSegSocial)
        self.__company: str = company
        self.__rate: float
        self.__hours: float
        self.rate = rate
        self.hours = hours

    def __str__(self) -> str:
        return f"{super().__str__()} company: {self.company}"

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
        """
        Set hours for this consultant
        **PRE:** hours must be >= 0
        """
        if hours < 0:
            print(f"hours must be >= 0 but the hours given was: {hours}", file=sys.stderr)
            return
        self.__hours = hours

    @rate.setter
    def rate(self, rate) -> None:
        """
        Set rate for this consultant
        **PRE:** rate must be >= 0
        """
        if rate < 0:
            print(f"rate must be >= 0 but the rate given was: {rate}", file=sys.stderr)
            return
        self.__rate = rate
