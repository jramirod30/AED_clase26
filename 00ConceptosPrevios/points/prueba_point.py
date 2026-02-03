from point import Point

p1: Point = Point(2, 3)

print(p1.x)

# p1.x = 5

p2: Point = Point(2, 3)

print(p1 == p2)

print(p1)
print(str(p1))
print(f"p2.X = {p2.x} p2.y = {p2.y}")
print(f"Private Attributes In Python OOP are Not Very Private X: {p2._Point__x}")
