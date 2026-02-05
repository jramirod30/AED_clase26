class A:
    public_class_attribute: str = "class A attribute"

    def __init__(self, data: int = 1):
        print("constructor class A")
        self.public_attrib: int = data
        self._protected_attrib: str = "protected !! "
        self.__private_attrib: float = data/3

    def soy(self) -> None:
        print(f"{type(self)}")

    def __str__(self) -> str:
        return f"value of public_attrib: {self.public_attrib} \t value of _protected_attrib: {self._protected_attrib}" \
               f" \t value of __private_attrib: {self.__private_attrib}"
