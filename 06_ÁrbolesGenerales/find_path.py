from typing import Iterator

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


def find_path[T](gtree: ITree[T], elem: T) -> list[IPosition[T]]:
    """
    PRE: gtree is not empty and not duplicated elems
    """
    return find_path_aux(gtree, elem, gtree.root, [])


def find_path_aux[T](gtree: ITree[T], elem: T,
                     p: IPosition[T], result: list[IPosition[T]]) -> list[IPosition[T]]:
    result.append(p)
    if p.element == elem:
        return result
    else:
        it: Iterator[IPosition[T]] = gtree.children(p)
        child_pos: IPosition[T] | None = next(it, None)
        aux: list[IPosition[T]] = []
        # As soon as elem is found in a subtree, it leaves the loop
        while aux == [] and child_pos is not None:
            aux = find_path_aux(gtree, elem, child_pos, result)
            child_pos = next(it, None)
        if aux:
            return aux
        else:
            result.pop()
            return []


print([p.element for p in find_path(tree, 9)])
print([p.element for p in find_path(tree, 999)])

