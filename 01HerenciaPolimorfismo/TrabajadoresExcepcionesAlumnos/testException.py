from enterprise import *


def input_str(fields: list[str]) -> list[str]:
    result: list[str] = []
    for ask in fields:
        result.append(input(ask))
    return result


def input_employee() -> Employee | None:
    end: bool = False
    employee_aux: Employee | None = None
    while not end:
        #  TODO using input_str, read the fields needed and
        #   creates an employee. You should add control
        #   for exceptions:  IncorrectSalary, IncorrectAge and Exception
        #   You must repeat the process until you get a new Employee
        pass

    return employee_aux


def input_manager() -> Manager | None:
    end: bool = False
    manager_aux: Manager | None = None
    while not end:
        #  TODO using input_str, read the fields needed and
        #   creates a manager. You should add control
        #   for exceptions:  IncorrectSalary, IncorrectAge and Exception
        #   You must repeat the process until you get a new Manager
        pass
    return manager_aux


# employee1: Employee = Employee(28, "Arthur", "SEG-2223", 1555.25)

employee1: Employee = input_employee()
print(f"employee read: {employee1}")
employee2: Employee = input_employee()
print(f"employee read: {employee2}")
manager1: Manager = input_manager()
print(f"manager read: {manager1}")
outsideConsultant1: OutsideConsultant = OutsideConsultant(37, "Philip", "SEG-666", 1.5, 10, "Compamy1")
# print(f"value of person1: {person1}")
# print(f"value of outSideConsultant1 {outsideConsultant1}")
