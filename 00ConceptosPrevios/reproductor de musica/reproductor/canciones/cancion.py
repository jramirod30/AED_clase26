from time import sleep


class Cancion:

    def __init__(self, titulo: str, duracion: float):
        self.__titulo: str = titulo
        self.__duracion: float = duracion
        self.__no_reproducciones: int = 0

    def reproducir_cancion(self) -> None:
        print(f"Reproduciendo cancion {self.__titulo}")
        self.__no_reproducciones += 1
        sleep(self.__duracion)

    def __eq__(self, other) -> bool:
        return self.__titulo == other.__titulo and self.__duracion == other.__duracion

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def duracion(self) -> float:
        return self.__duracion

    @property
    def no_reproducciones(self) -> int:
        return self.__no_reproducciones

    @no_reproducciones.setter
    def no_reproducciones(self, no_reproducciones: int) -> None:
        self.__no_reproducciones = no_reproducciones

    def __str__(self) -> str:
        return f"({self.__titulo}, {self.__duracion}, {self.__no_reproducciones})"
