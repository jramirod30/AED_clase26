from . import Animal
from . import Pet


class Dog(Animal, Pet):

    def __init__(self, name: str = "", owner: str = ""):
        Animal.__init__(self, "Guagua!!")
        Pet.__init__(self, name, owner)

    def lick_bone(self) -> None:
        print(f"{self.name} is licking a bone!!!!!!")

    def __str__(self) -> str:
        return f"I am a dog with " \
               f"{Pet.__str__(self)} and {Animal.__str__(self)}"
