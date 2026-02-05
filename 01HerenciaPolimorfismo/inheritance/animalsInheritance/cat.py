from . import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__("Miau!!")

    def play_ball(self) -> None:
        print("Having fun playing with a ball!")
