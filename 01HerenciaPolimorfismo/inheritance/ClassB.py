from inheritance.accessLevel.classA import A


class B(A):
    def __init__(self):
        print("subclass B constructor")
        super().__init__(5)

    def print_public(self) -> None:
        print(f"public attribute {self.public_attrib}")

    def print_protected(self) -> None:
        print(f"protected attribute {self._protected_attrib}")

    def print_private(self) -> None:
        # self.__private_attrib = "hiding private attribute from father"
        print(f"private attribute {self.__private_attrib}")
