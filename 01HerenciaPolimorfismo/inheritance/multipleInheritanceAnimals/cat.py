from . import Animal
from . import Pet


class Cat(Animal, Pet):
    # In python there is not overloading so, we will use default values
    def __init__(self, name: str = "", owner: str = ""):
        Animal.__init__(self, "Miau!!")
        Pet.__init__(self, name, owner)

    def play_ball(self) -> None:
        print(F'{self.name} has fun playing with wool ball!')

    def __str__(self) -> str:
        return f"I am a cat with " \
               f"{Pet.__str__(self)} and {Animal.__str__(self)}"
