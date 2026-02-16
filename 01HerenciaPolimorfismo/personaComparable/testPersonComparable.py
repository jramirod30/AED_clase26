from typing import List

from person import Person
from person import Person2


def list2_string(data: List[Person]) -> str:
    result: str = ""
    for person_data in data:
        result += person_data.__str__() + "\n"
    return result


def main() -> None:
    def no_eq() -> None:
        # For person2 == is equivalent to operator "is"
        person1: Person2 = Person2("Mary", "Alonso", 25)
        person2: Person2 = Person2("Mary", "Alonso", 25)
        person3: Person2 = Person2("Peter", "Alonso", 34)
        person4: Person2 = person3
        print(f"{person1} is equal to {person2}? {person1 == person2}")
        print(f"{person1} is equal to {person3}? {person1 == person3}")
        print(f"{person3} is equal to {person4}? {person3 == person4}")

    def yes_eq() -> None:
        person1: Person = Person("Mary", "Alonso", 25)
        person2: Person = Person("Mary", "Alonso", 25)
        person3: Person = Person("Peter", "Alonso", 34)
        person4: Person = Person("Mary", "Alba", 28)
        print(f"{person1} is equal to {person2}? {person1 == person2}")
        print(f"{person1} is equal to {person3}? {person1 == person3}")
        print(f"{person1} is greater than {person2}? {person1 > person2}")
        print(f"{person1} is greater than {person3}? {person1 > person3}")
        print(f"{person3} is greater than {person1}? {person3 > person1}")
        print(f"{person1} is less than {person3}? {person1 < person3}")
        print(f"{person3} is less than {person1}? {person3 < person1}")
        print(f"{person1} is less equals than {person4}? {person1 <= person4}")
        print(f"{person4} is less equals than {person1}? {person4 <= person1}")
        person_list: List[Person] = [person1, person3, person4, person2]
        print(f"Sorted list for \n{list2_string(person_list)}")
        person_list.sort()
        print(f"is: \n{list2_string(person_list)}")

    no_eq()
    print("Using person with override ==")
    yes_eq()


if __name__ == '__main__':
    main()
