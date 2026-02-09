from typing import override

class Person:
    """
    This class represent a person
    """
    def __init__(self, name: str, age: int):
        """
        Constructor for person
        :param age: person age. It must be >= 0
        :param name: names' person
        """
        self.__age: int  # <-- private age attribute was defined
        self.__name: str = name
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
        return f"name: {self.__name} age: {self.__age}"

    """
    Properties definition
    """
    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 0:
            raise ValueError("age must be >= 0")
        self.__age = age
