from typing import override
from school import Student

class FaceToFaceStudent(Student):

    def __init__(self, name: str, age: int, class_num: int,
                 academic_level: str,
                 n_exam_call: int, overrun_per_exam_call: float,
                 school_year_fee: float):
        super().__init__(name, age, class_num, academic_level)
        self.__n_exam_call = n_exam_call
        self.__overrun_per_exam_call = overrun_per_exam_call
        self.__school_year_fee = school_year_fee

    @override
    def get_subjects(self) -> str:
        return f"All subjects for class {self.class_num}"

    @override
    def monthly_rate(self) -> float:
        return (self.__school_year_fee +
                self.__overrun_per_exam_call * self.__n_exam_call) / 12
