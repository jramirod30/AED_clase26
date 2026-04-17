from tads import IBinaryTree, LinkedBinaryTree, IPosition

tree: IBinaryTree[int] = LinkedBinaryTree()

root: IPosition[int] = tree.add_root(1)

n2: IPosition[int] = tree.add_left(root, 2)
tree.add_left(n2, 4)
tree.add_right(n2, 5)

n3: IPosition[int] = tree.add_right(root, 3)
tree.add_left(n3, 6)
n7: IPosition[int] = tree.add_right(n3, 7)
tree.add_left(n7, 8)

print(tree)


def contar_hojas_aux[T](btree: IBinaryTree[T], p: IPosition[T] | None) -> int:
    if p:
        if btree.is_leaf(p):
            return 1
        else:
            return (contar_hojas_aux(btree, btree.left(p)) +
                    contar_hojas_aux(btree, btree.right(p)))
    else:
        return 0


def contar_hojas[T](btree: IBinaryTree[T]) -> int:
    return contar_hojas_aux(btree, btree.root)


print(contar_hojas(tree))


def contar_ocurrencias[T](btree: IBinaryTree[T], elem: T) -> int:
    def contar_ocurrencias_aux[T](btree: IBinaryTree[T], elem: T,
                                  p: IPosition[T] | None) -> int:
        if p:
            return ((1 if p.element == elem else 0) +
                    contar_ocurrencias_aux(btree, elem, btree.left(p)) +
                    contar_ocurrencias_aux(btree, elem, btree.right(p)))
        else:
            return 0

    return contar_ocurrencias_aux(btree, 3, btree.root)


def find[T](btree: IBinaryTree[T], elem: T) -> IPosition[T] | None:
    def find_aux(btree: IBinaryTree[None], elem: T, p: IPosition[T] | None) -> IPosition[T] | None:
        if p is None:
            return None
        if p.element == elem:
            return p
        resultado: IPosition[T] | None = (
            find_aux(btree, elem, btree.left(p)))
        if resultado is not None:
            return resultado
        return find_aux(btree, elem, btree.right(p))

    return find_aux(btree, elem, btree.root)


def separar_pares_aux(btree: IBinaryTree[int],
                      p: IPosition[int] | None) -> list[int]:
    if p:
        return ([p.element] if p.element % 2 == 0 else []) + \
            separar_pares_aux(btree, btree.left(p)) + \
            separar_pares_aux(btree, btree.right(p))
    else:
        return []


def separar_pares(btree: IBinaryTree[int]) -> list[int]:
    return separar_pares_aux(btree, btree.root)

def separar_pares_aux1(btree: IBinaryTree[int],
                      p: IPosition[int] | None, lista: list[int]) -> list[int]:
    if p:
        if p.element % 2 == 0:
            lista.append(p.element)
        separar_pares_aux1(btree, btree.left(p), lista)
        separar_pares_aux1(btree, btree.right(p), lista)
        return lista
    else:
        return lista


def separar_pares1(btree: IBinaryTree[int]) -> list[int]:
    return separar_pares_aux1(btree, btree.root, [])