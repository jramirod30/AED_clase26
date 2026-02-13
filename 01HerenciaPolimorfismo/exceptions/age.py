from datetime import datetime

from unrealAgeException import UnrealAgeException


def ask_for_age() -> int:
    age_str: str = input("age?: ")
    if not age_str.isnumeric():
        raise ValueError("given age is not a natural number")
    return int(age_str)

def ask_for_age2(age_lower_limit: int = 0, age_upper_limit: int = 200) -> int:
    age_str: str = input("age?: ")
    if not age_str.isnumeric():
        raise ValueError("given age is not a natural number")
    age_int: int = int(age_str)
    if age_int > age_upper_limit or age_int < age_lower_limit:
        raise UnrealAgeException(f"error unreal age!! the given age is:{age_str}")
    return age_int


end: bool = False
age: int = 0
while not end:
    try:
        age = ask_for_age()
        current_year = datetime.now().year
        print("You were born in year:", current_year - age)
        end = True  # If age given is valid this sentence will be executed
    except ValueError as e:
        print(f"{e}, try again")


end: bool = False
age: int = 0
while not end:
    try:
        age = ask_for_age2()
        current_year = datetime.now().year
        print("You were born in year:", current_year - age)
        end = True  # If age given is valid this sentence will be executed
    except ValueError as e:
        print(e, ", try again")
    except UnrealAgeException as e:
        print(f"{e}, unbelievable age!!!")
        end = True  # loop exit is forced after this exception
print("End")
