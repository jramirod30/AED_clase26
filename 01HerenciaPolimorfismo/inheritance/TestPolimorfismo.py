from multipleInheritanceAnimals import *

"""
These sentences show polymorphism in POO way
"""


def print_data(data_list: list[Animal]):
    for datum in data_list:
        print(f"Datos animal: {datum}")


cat2: Animal = Cat("Blacky", "Mary")
dog1: Animal = Dog("Pluto", "Mickey")
sheep1: Sheep = Sheep("Juan")

# ListAnimales = list[Animal]
data: list[Animal] = []

data.append(sheep1)
data.append(dog1)
data.append(cat2)
"""
Python is polymorphic per se, the next sentence illustrates the polymorphism in python way
"""
# This sentence produces a Warning in some IDES likes PyCharm, but
# this sentence will work and data will contain animals and strings
data.append("I am not an animal I am a String")
print_data(data)

data2: list = []
data2.append(sheep1)
data2.append(dog1)
data2.append(cat2)
# This sentence doesn't produce a Warning
data2.append("I am not an animal I am a String")
print("Printing data2 a python way for polymorphic")
print_data(data2)
