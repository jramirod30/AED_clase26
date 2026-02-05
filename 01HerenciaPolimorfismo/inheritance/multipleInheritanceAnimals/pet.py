class Pet:
    # Keep in mind that this is a class attribute.
    # in python if a class attribute is changed in an instance a new one attribute is defined
    # __name: str
    # __owner: str

    def __init__(self, name: str, owner: str):
        self.__name: str = name
        self.__owner: str = owner

    def __str__(self) -> str:
        return f"name {self.name} and" \
               f" age {self.owner}"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def owner(self) -> str:
        return self.__owner
