
class Person:
    """
    This class represent a person
    """

    def __init__(self, age: int, name: str, surname: str = ""):
        """
        Constructor for person
        **PRE:** age >= 0
        :param age: person age. It must be >= 0
        :param name: names' person
        """
        self.__age: int  # <-- private age attribute was defined
        self.age = age  # <-- set age through its property
        self.__name: str = name
        self.__surname = surname

    """
    Methods definition
    """

    def __str__(self) -> str:
        """
        Overwrite string conversion method (to String)
        :return: string that represent the object
        """
        return f"Name: {self.__name} surname: {self.__surname} age: {self.__age}"

    def __eq__(self, other) -> bool:
        """
        Overwrite operator ==
        """
        return self.__name == other.__name and self.__surname == other.__surname \
            and self.__age == other.__age

    def __lt__(self, other):
        return self.__surname < other.__surname or \
               (self.__surname == other.__surname and
                self.__name < other.__name)

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
    def age(self, age: int) -> None:
        if age < 0:
            raise ValueError("age must be >= 0")
        self.__age = age
