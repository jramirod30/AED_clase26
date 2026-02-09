from school import FaceToFaceStudent
from school import FreeStudent
from school import Student

def list_subject(students: list[Student]) -> None:
    for student in students:
        print(f"{student.get_subjects()}")


def total_payments(students: list[Student]) -> float:
    total: float = 0
    for student in students:
        total += student.monthly_rate()
    return total


def print_all_students(students: list[Student]) -> None:
    for student in students:
        print(student)

def test_school():
    students: list[Student] = [FreeStudent("John", 19, 2, "Entry level", 5),
                               FaceToFaceStudent("Sheila", 18, 1,
                                                 "Diploma", 0, 50.30, 1900),
                               FreeStudent("Mary", 21, 3, "bachelor of science", 7),
                               FaceToFaceStudent("Peter", 20, 2,
                                                 "Foundation Degrees", 2, 50.30, 2200)
                               ]
    list_subject(students)
    print(f"Total revenue {total_payments(students)}\n")
    print("---------------- student data-----------------")
    print_all_students(students)


if __name__ == '__main__':
    test_school()
