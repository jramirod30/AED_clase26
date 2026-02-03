from point import Point
from copy import copy
point1: Point = Point(3, 4)
point2: Point = point1  # copy reference
point3: Point = copy(point1)  # point3 is a copy of point1
print(f"point1: {point1} and memory address for point1 {id(point1)}\n"
      f"point2: {point2} and memory address for point2 {id(point2)}\n"
      f"point3: {point3} and memory address for point3 {id(point3)}")


# function __eq__ will be used for operator ==.
# Operator 'is' return true if the references are the same
print(f"point1 is point2: {point1 is point2} point3 is point1 {point3 is point1}")
print(f"point1 == point2: {point1 == point2} point3 == point1 {point3 == point1}")
# print(point1.__x) provokes a warning, because private attribute x
# is not visible in this scope
# modify x in point1
point1.x = -3
# A new attribute in this context is defined,
# but it is not affected to private attribute x
point1.__x = 55
print("after point1.x = -3")
print(f"point1: {point1} point2: {point2} point3: {point3}")
print(f"point1 is point2: {point1 is point2} point3 is point1 {point3 is point1}")
print(f"point1 == point2: {point1 == point2} point3 == point1 {point3 == point1}")
print(f"attrib {point1.__dict__}")
