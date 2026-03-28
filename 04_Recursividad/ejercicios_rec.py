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

