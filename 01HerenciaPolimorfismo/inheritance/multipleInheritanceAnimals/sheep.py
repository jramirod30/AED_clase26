from . import Animal


class Sheep(Animal):
    def __init__(self, shepherd: str = ""):
        super().__init__("Beee!")
        self.__shepherd: str = shepherd

    def graze(self) -> None:
        print("grazing grass!!")

    @property
    def shepherd(self) -> str:
        return self.__shepherd

    def __str__(self) -> str:
        return f"I am a sheep and my shepherd is {self.__shepherd}" \
               f" and {super().__str__()}"  # <-- calling to string from father
