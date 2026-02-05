from reproductor.canciones.cancion import Cancion


class ReproductorMusica:

    def __init__(self):
        self.__canciones: list[Cancion] = []
        self.__puntero: int = -1  # no apunta a ninguna canción

    def __str__(self) -> str:
        result: str = "("
        end: str = ", "
        for i in range(len(self.__canciones) - 1):
            result += str(self.__canciones[i]) + end
        result += ")" if len(self.__canciones) < 1 else\
            f"{str(self.__canciones[-1])}), punt={self.__canciones[self.__puntero]} "
        return result

    def insertar_canciones(self, canciones: list[Cancion]) -> None:
        """
        PRE: cierto

        POST: Inserta las canciones en la biblioteca (al final).
              Deja el puntero apuntando a la primera canción dada.
              Utiliza las canciones del vector dado.
        """
        self.__puntero = len(self.__canciones)
        self.__canciones += canciones

    def reproducir_cancion_seleccionada(self) -> None:
        """
        PRE: la lista no está vacía

        POST: reproduce la canción a la que apunta el puntero
        """
        pass

    def avanzar_puntero(self) -> None:
        """
        PRE: la lista no está vacía y el puntero no está en la última canción

        POST: avanza el puntero a la siguiente canción de la lista
        """
        pass

    def hay_siguiente(self) -> bool:
        """
        POST: Indica si hay al menos una canción desde la posición actual del puntero
        """
        pass

    def __buscar_cancion(self, titulo: str, duracion: int) -> int:
        """
        POST: Si hay una canción con el título y la duración dadas, devuelve su posición
              e.o.c. devuelve -1
        """
        pass

    def seleccionar_cancion(self, titulo: str, duracion: int) -> None:
        """
        POST: Si la canción existe, pone el puntero en la primera ocurrencia
              de la canción con el título y la duración dados
              e.o.c. deja el puntero igual
        """
        pass

    def borrar_cancion(self, titulo: str, duracion: int) -> None:
        """
        POST: Si la canción dada está en la biblioteca,
              borra la primera ocurrencia de la canción y
              deja el puntero apuntando a la primera canción, si existe
              e.o.c. no hace nada
        """
        pass

    def seleccionar_canciones_mas_escuchadas(self, veces: int = 2) -> list[Cancion]:
        """
        POST: Devuelve una lista con copias de las canciones que
              se han escuchado igual o más de un número dado de veces.
              Si no hay ninguna, se devuelve una lista de tamaño cero.
        """
        pass
