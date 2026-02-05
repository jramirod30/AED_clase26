class Animal:
    # Keep in mind that this is a class attribute.
    # in python if a class attribute is changed in an instance method (self.)
    # a new one instance attribute is defined
    # __sound: str = None

    def __init__(self, sound: str):
        self.__sound: str = sound

    def play_sound(self) -> None:
        print(self.__sound)

    # We have defined sound as property and get method is provided
    @property
    def sound(self) -> str:
        return self.__sound
