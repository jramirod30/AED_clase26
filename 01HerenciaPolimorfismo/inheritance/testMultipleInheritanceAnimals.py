# from typing import List

from multipleInheritanceAnimals import *


cat2: Animal = Cat("Blacky", "Mary")
pet1: Pet = Dog("Pluto", "Mickey")
sheep1: Sheep = Sheep()

print(f"to string oveja1 {sheep1}")
print(f"to string mascota1 {pet1}")
print(f"to string gato2 {cat2}")

print(f"my name is {pet1.name} and the name of my owner is {pet1.owner}")
# To avoid runtime errors, you must ensure that the instance, is a dog instance
# before you call to lick_bone.
# Python, allows us to call lick_bone without further verifications,
# but at risk of provoking a runtime error
if isinstance(pet1, Dog):
    pet1.lick_bone()

pet1 = cat2  # IDE warning: Expected type 'Pet', got 'Animal' instead
print(f"my name is {pet1.name} and the name of my owner is {pet1.owner}")

# pet1.lick_bone()  # <--- runtime error
if isinstance(pet1, Dog):
    pet1.lick_bone()
elif isinstance(pet1, Cat):
    pet1.play_ball()

print(pet1)

