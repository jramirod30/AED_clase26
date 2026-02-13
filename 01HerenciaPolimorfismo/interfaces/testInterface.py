from figures import IFigure
from figures import CircularMirror
from figures import Photo


def total_area(figures: list[IFigure]) -> float:
    total: float = 0
    for figure in figures:
        total += figure.area()
    return total


figures2: list[IFigure] = [CircularMirror(10), Photo(12, 5), Photo(10, 14), CircularMirror(5)]
print(f"Total area: {total_area(figures2)}")
