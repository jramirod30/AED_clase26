# from inheritance.animals.perro import Dog
# from inheritance.animals.gato import Cat
# from inheritance.animals.oveja import Sheep
# Si se importan todos en __init__.py se puede poner esto
from animals import *

dog: Dog = Dog()
cat: Cat = Cat()
sheep: Sheep = Sheep()
dog.play_sound()
cat.play_sound()
sheep.play_sound()
