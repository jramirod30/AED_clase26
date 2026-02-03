class BankAccount:
    """
    This class represents a bank account
    """
    __opening_expenditure: float = 10
    """
    Opening expenditure
    """
    __interest_rate: float = 0.1
    """
    Annual rate
    """

    def __init__(self, amount: float, hide_class: bool = False):
        """
        PRE: amount > = opening expenditure
        :param amount: initial bank balance
        """
        self.__bank_balance: float = amount - BankAccount.__opening_expenditure
        if hide_class:
            # Creating an instance attribute hiding class attribute.
            # So, from now this instance has got BankAccount.__interest_rate_2 and self.__interest_rate_2
            self.__interest_rate: float = 0.75

    def __str__(self) -> str:
        return f"bank balance: {self.bank_balance} " \
               f"class attributes Opening expenditure: {BankAccount.get_opening_expenditure()} " \
               f"class attributes interest rate: {BankAccount.get_interest_rate()}"

    @property
    def bank_balance(self):
        return self.__bank_balance

    def deposit(self, amount: float) -> None:
        """
        Add amount to bank balance
        PRE: amount > 0
        :param amount:
        :return:
        """
        self.__bank_balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from bank account
        PRE: amount > 0 and amount < bank balance
        :param amount:
        :return:
        """
        self.__bank_balance -= amount

    #  classifier methods
    @staticmethod
    def get_opening_expenditure() -> float:
        return BankAccount.__opening_expenditure



    @staticmethod
    def set_opening_expenditure(expenditure: float) -> None:
        BankAccount.__opening_expenditure = expenditure

    @classmethod
    def get_interest_rate(cls) -> float:
        return cls.__interest_rate

    @classmethod
    def set_interest_rate(cls, rate: float) -> None:
        cls.__interest_rate = rate

    def get_interest_rate2(self) -> float:
        # You can get access to a class attribute using self reference
        return self.__interest_rate
