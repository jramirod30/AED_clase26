from animalsInheritance import *

animal1: Animal = Animal("Cuack")
if isinstance(animal1, Cat):  # test if animal1 is a Cat instance
    animal1.play_ball()  # Not waring due to previous if
else:
    print("animal1 is not a cat")

cat1: Cat = Cat()
cat2: Animal = Cat()  # Upcasting

cat2.play_ball()  # Waring due there is not test to know if cat2 is an instance of Cat

if isinstance(cat2, Cat):
    print("cat2 is a cat")
    cat2.play_ball()  # but you can use method or properties from a subclass. No Warning is given due to if sentence

dog1: Dog = Dog()

animal1.play_sound()
print(animal1.sound)   # sound is a property, so we can get its value without a get method
cat1.play_sound()
print(cat2.sound)
cat1.play_ball()

if isinstance(animal1, Cat):
    animal1.play_ball()
else:
    print("animal1 is not a cat")

sheep1: Sheep
sheep2: Animal = Sheep("Juan")
# sheep1 = sheep2  # IDE Warning: Expected type 'Sheep', got 'Animal' instead

if isinstance(sheep2, Sheep):
    sheep1 = sheep2  # Not waring due to previous if. downcasting verify
    sheep1.graze()
    print(f"shepherd: {sheep1.shepherd}")
