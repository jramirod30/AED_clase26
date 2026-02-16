from person import Person

def order_by_name(data: list[Person], reverse: bool= False) -> None:
    """
    Ordena la lista pasada como parámetro por apellido y nombre
    :param data:
    :return:
    """
    data.sort(reverse=reverse)

def order_by_age(data: list[Person], reverse: bool = False) -> None:
    """
    Ordena la lista pasada como parámetro por edad
    :param data:
    :return:
    """
    data.sort(key=sorting_criteria, reverse=reverse)
    # data.sort(key=lambda person: person.age, reverse=reverse)

def sorting_criteria(person: Person) -> int:
    return person.age

persona1: Person = Person("Pepe", "Garcia", 34)
persona2: Person = Person("Ana", "Gonzalez", 32)
persona3: Person = Person("Pepe", "Garcia", 34)

print(persona1 == persona3)

persons: list[Person] = [persona1, persona2, Person("Luis", "Blanco", 45),
                         Person("Juan", "Zanja", 33)]

# Sort by surname and name
# Person overrides magic methods for <, >, >=, >=, == and !=
print("Sort by surname and name")
order_by_name(persons)
for person in persons:
    print(person)

# Sort by age
print("Sort by age")
# key define a function to get the value that should be used to compare elements
# in this example age will be used
order_by_age(persons)
for person in persons:
    print(person)
