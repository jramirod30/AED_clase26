import sys


def xor(lista1: list[int], lista2: list[int]) -> list[int]:
    if len(lista1) < 1:
        return []
    elif lista1[0] == lista2[0]:
        return [0] + xor(lista1[1:], lista2[1:])
    else:
        return [1] + xor(lista1[1:], lista2[1:])


def xor1(lista1: list[int], lista2: list[int], i: int = 0) -> list[int]:
    if len(lista1) == i:
        return []
    elif lista1[i] == lista2[i]:
        return [0] + xor1(lista1, lista2, i + 1)
    elif lista1[i] != lista2[i]:
        return [1] + xor1(lista1, lista2, i + 1)


def intercalar[T](lista1: list[T], lista2: list[T], i: int = 0) -> list[T]:
    if i < len(lista1) and i < len(lista2):
        return [lista1[i]] + [lista2[i]] + intercalar(lista1, lista2, i + 1)
    elif i < len(lista1):
        return lista1[i:]
    else:
        return lista2[i:]


def quicksort[T](lista: list[T]) -> list[T]:
    if len(lista) <= 1:
        return lista
    else:
        pivote: T = lista[0]
        menor: list[T] = []
        mayor: list[T] = []
        for i in lista[1:]:
            if i < pivote:
                menor.append(i)
            else:
                mayor.append(i)
        return quicksort(menor) + [pivote] + quicksort(mayor)


def borrar_todos[T](lista: list[T], elem: T, i: int = 0) -> None:
    if i < len(lista):
        if lista[i] == elem:
            lista.pop(i)
            borrar_todos(lista, elem, i)
        else:
            borrar_todos(lista, elem, i + 1)


def insertar_ord(lista: list[int], elem: int, i: int = 0) -> None:
    if i < len(lista):
        if lista[i] >= elem:
            lista.insert(i, elem)
        else:
            insertar_ord(lista, elem, i + 1)
    else:
        lista.append(elem)


lista_test: list[int] = [1, 3, 5, 7, 9, 11]
insertar_ord(lista_test, 13)
print(lista_test)


def palindroma(palabra: str, i: int = 0):
    if i >= (len(palabra) / 2):
        return True
    else:
        return (palabra[i] == palabra[len(palabra) - 1 - i]
                and palindroma(palabra, i + 1))


def maximo_lista(lista: list[int], max_t: int = -sys.maxsize,
                 i: int = 0) -> int:
    if i < len(lista):
        return (maximo_lista(lista, lista[i], i + 1) if lista[i] > max_t
                else maximo_lista(lista, max_t, i + 1))
    else:
        return max_t
