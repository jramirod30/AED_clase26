from inheritance.accessLevel.classA import A
from inheritance.ClassB import B


class D:
    data: A = A()
    data2: B = B()

    def __init__(self):
        self.data2._protected_attrib += " class D"

    def print_public(self):
        print(f"public in D {self.data.public_attrib}")

    def print_protected(self):
        print(f"protected in D {self.data2._protected_attrib}")


"""d: D = D()
d.print_public()
d.print_protected()
"""