from person.person import Person

class Worker(Person):
    """
    This class define a worker
    """
    def __init__(self, age: int, name: str, nSegSocial: str):
        super().__init__(age, name)
        self.__nSegSocial = nSegSocial

    @property
    def nSegSocial(self) -> str:
        return self.__nSegSocial
