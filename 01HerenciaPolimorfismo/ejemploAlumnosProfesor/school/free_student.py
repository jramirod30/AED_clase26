from typing import override
from school import Student


class FreeStudent(Student):
    # class attribute
    __rate_hour: float = 10  # Rate per hour
    # Working day per month
    # __WORKING_DAY_PER_MONTH: int = 20  # in python doesn't exist constant

    @classmethod
    @property
    def __WORKING_DAY_PER_MONTH(cls) -> int:
        return 20


    def __init__(self, name: str, age: int, class_num: int,
                 academic_level: str, hours_per_day: int):
        super().__init__(name, age, class_num, academic_level)
        self.__hours_per_day = hours_per_day
        self.__subject_list: list[str] = []
        self.__retrieve_subjects()

    #  This method must retrieve subjects from server or database
    #  Its implementation is not relevant for this example
    def __retrieve_subjects(self):
        pass

    @override
    def get_subjects(self) -> str:
        subjects = f"Subjects for {self.name}: "
        for subject in self.__subject_list:
            subjects += subject + " "
        return subjects

    @override
    def monthly_rate(self) -> float:
        return self.__hours_per_day * \
               FreeStudent.__rate_hour * \
               FreeStudent.__WORKING_DAY_PER_MONTH
