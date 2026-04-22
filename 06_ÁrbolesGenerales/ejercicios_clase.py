from tads import IGeneralTree, IPosition, LinkedGeneralTree, \
                  ITree

tree: IGeneralTree[int] = LinkedGeneralTree()
p1: IPosition[int] = tree.add_root(1)
p2: IPosition[int] = tree.add_child_first(p1, 2)
p3: IPosition[int] = tree.add_child_last(p1, 3)

tree.insert_sibling_before(p3, 10)
p4: IPosition[int] = tree.add_child_first(p2, 4)
p6: IPosition[int] = tree.insert_sibling_after(p4, 6)
tree.insert_sibling_before(p6, 5)
tree.add_child_first(p3, 7)
tree.add_child_first(tree.add_child_last(p3, 8), 9)

print(tree)

def contar_nodos_internos[T](gtree: ITree[T]) -> int:
    def contar_nodos_internos_aux[T](pos: IPosition) -> int:
        total: int = 0
        if not gtree.is_leaf(pos):
            total += 1
            child_pos: IPosition[T]
            for child_pos in gtree.children(pos):
                total += contar_nodos_internos_aux(child_pos)
            return total
        else:
            return 0
    return contar_nodos_internos_aux(gtree.root)


print(contar_nodos_internos(tree))

def depth[T](gtree: ITree[T], p: IPosition[T]) -> int:
