def suma(lista: list[int], i: int = 0) -> int:
    if i < len(lista):
        return lista[i] + suma(lista, i + 1)
    else:
        return 0


print(suma([1, 2, 3]))


def multiplicar10(lista: list[int]) \
        -> list[int]:
    if len(lista) < 1:
        return []
    else:
        return [lista[0] * 10] + multiplicar10(lista[1:])


print(multiplicar10([1, 2, 3]))


def multiplicar10_1(lista: list[int], i: int = 0) -> list[int]:
    if i == len(lista):
        return []
    return [lista[i] * 10] + multiplicar10_1(lista, i + 1)


def multiplicar10_2(lista: list[int], i: int) -> list[int]:
    if i < 0:
        return []
    aux: list[int] = multiplicar10_2(lista, i - 1)
    aux.append(lista[i] * 10)
    return aux


print(multiplicar10_2([1, 2, 3], 2))


def posiciones_recursividad[T](lista: list[T], dato: T, i: int = 0) \
        -> list[int]:
    if len(lista) == i:
        return []
    elif lista[i] == dato:
        return [i] + posiciones_recursividad(lista, dato, i + 1)
    else:
        return posiciones_recursividad(lista, dato, i + 1)


print(posiciones_recursividad([1, 2, 3, 3, 3, 3, 4, 5], 3))


def posiciones_recursividad1[T](lista: list[T], dato: T, i: int) \
        -> list[int]:
    if i < 0:
        return []
    elif lista[i] == dato:
        aux: list[int] = posiciones_recursividad1(lista, dato, i - 1)
        aux.append(i)
        return aux
    else:
        return posiciones_recursividad1(lista, dato, i - 1)


print(posiciones_recursividad1([1, 2, 3, 3, 3, 3, 4, 5], 3, 7))


def buscar_indice[T](lista: list[T], elem: T, i: int = 0,
                     sol: list[int] = []) \
        -> list[int]:
    if len(lista) == i:
        return sol
    if lista[i] == elem:
        sol.append(i)
    return buscar_indice(lista, elem, i + 1, sol)


print(buscar_indice([1, 2, 3, 3, 3, 3, 4, 5], 3))
