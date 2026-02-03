from reproductor.canciones.cancion import Cancion
from reproductor.reproductor_musica1 import ReproductorMusica


def main() -> None:

    canciones = [Cancion("A", 2), Cancion("B", 1), Cancion("C", 1)]

    player: ReproductorMusica = ReproductorMusica()

    player.insertar_canciones(canciones)

    print(f"player tras insertar las canciones:{player}")
    print("Se reproducen todas las canciones")
    while player.hay_siguiente():
        player.reproducir_cancion_seleccionada()
        player.avanzar_puntero()
    print("Fin reproducción")
    print("Se reproduce la canción seleccionada dos veces")
    player.reproducir_cancion_seleccionada()
    player.reproducir_cancion_seleccionada()
    print("Se selecciona la canción B con duración 1")
    player.seleccionar_cancion("B", 1)
    print("Se reproduce la canción seleccionada dos veces")
    player.reproducir_cancion_seleccionada()
    player.reproducir_cancion_seleccionada()
    print(f"Estado del reproductor {player}")

    print("Se intenta seleccionar una canción que no existe")
    player.seleccionar_cancion("D", 1)

    print(f"Estado del reproductor {player}")
    print('Se inserta la canción ("D",1)')
    player.insertar_canciones([Cancion("D", 1)])
    print('Se intenta borrar una canción que no existe: ("A", 1)')
    player.borrar_cancion("A", 1)

    print(f"Estado del reproductor {player}")
    print("Se muestran las canciones más escuchadas (número de veces >=2)")
    for cancion in player.seleccionar_canciones_mas_escuchadas():
        print(cancion)


if __name__ == "__main__":
    main()
