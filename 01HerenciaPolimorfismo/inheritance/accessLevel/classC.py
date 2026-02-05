from inheritance.accessLevel.classA import A
from inheritance.ClassB import B


class C:
    data: A = A()
    data2: B = B()

    def print_public(self) -> None:
        print(f"public in C {self.data.public_attrib}")

    def print_protected(self) -> None:
        print(f"protected in C {self.data._protected_attrib}")
