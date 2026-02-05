from . import Animal


class Sheep(Animal):
    def __init__(self, shepherd: str = ""):
        Animal.__init__(self, "Beee!")
        self.__shepherd: str = shepherd

    def graze(self) -> None:
        print("grazing grass!!")

    @property
    def shepherd(self) -> str:
        return self.__shepherd
