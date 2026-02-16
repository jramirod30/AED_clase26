class Person2:
    """
    This class represent a person and not override operators == != <, > ..
    """

    def __init__(self, name: str, surname: str, age: int):
        """
        Constructor for person
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
