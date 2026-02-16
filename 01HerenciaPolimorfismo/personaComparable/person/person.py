from typing import override


class Person:
    """
    This class represent a person and override operators == != <, > ...
    """

    def __init__(self, name: str, surname: str, age: int):
        """
        Constructor for Person
        :param age: person age. It must be >= 0
        :param name: names' person
        """
        self.__name: str = name
        self.__surname: str = surname
        self.__age: int  # <-- private age attribute was defined
        self.age = age  # <-- set age through its property

    """
    Methods definition
    """
    @override
    def __str__(self) -> str:
        """
        Overwrite string conversion method (to String)
        :return: string that represent the object
        """
        return f"surname: {self.surname} name: {self.name} age: {self.age}"

    """
    Properties definition
    """

    @property
    def name(self) -> str:
        return self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 0:
            raise ValueError("age must be >= 0")
        self.__age = age

    """
    Override operators 
    """
    @override
    def __eq__(self, other):
        """
        Override eq
        :param other: info to compere
        :return: true if name and surname are equals
        """
        return isinstance(other, Person) and other.name == self.name \
            and other.surname == self.surname

    # Next methods do not admit @override decorator due to these methods are abstract, and they are ‘magics’ methods too

    def __gt__(self, other):
        """
        Override >
        :param other: info to compare.
        :return: true if self.surname > other.surname or
        (self.surname == other.surname and self.name > other.name) other wise return false
        """
        return isinstance(other, Person) and \
            (self.surname > other.surname or
             (self.surname == other.surname and self.name > other.name))

    def __lt__(self, other):
        """
        Override <
        :param other: info to comparare
        :return: true if self.surname < other.surname or
        (self.surname == other.surname and self.name < other.name) other wise return false
        """
        return isinstance(other, Person) and \
            (self.surname < other.surname or
             (self.surname == other.surname and self.name < other.name))

    def __ge__(self, other):
        """
        Override >=
        :param other: info to compare
        :return: true if self is greater or equal than other
        """
        return not self < other

    def __le__(self, other):
        """
        Override <=
        :param other: info to compare
        :return: true if self is less or equal than other
        """
        return not self > other
