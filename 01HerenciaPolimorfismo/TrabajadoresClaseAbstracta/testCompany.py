from enterprise.employee import Employee
from enterprise.manager import Manager
from enterprise.outsideConsultant import OutsideConsultant
from enterprise.worker import Worker
from person.person import Person

def calculate_total_payments(workers: list[Worker]) -> float:
    total: float = 0
    for worker in workers:
        total += worker.monthly_payment()
    return total


person1: Person = Person(age=22, name="Mary")
print(f"value of person1: {person1}")
# worker1: Worker = Worker(23, "Jonh", "SEG-100")
employee1: Employee = Employee(28, "Arthur", "SEG-2223", 13000)
manager1: Manager = Manager(43, "Angel", "SEG-225", 18000, 200)
outsideConsultant1: OutsideConsultant = OutsideConsultant(37, "Philip", "SEG-666", 1.5, 10, "Compamy1")

company_workers: list[Worker] = [employee1, manager1, outsideConsultant1]

print(f"Coste mensual de los trabajadores: {calculate_total_payments(company_workers)}")
