from . import Animal


class Dog(Animal):

    def __init__(self):
        super().__init__("Guagua!!")

    def lick_bone(self) -> None:
        print("is licking a bone!!!")
