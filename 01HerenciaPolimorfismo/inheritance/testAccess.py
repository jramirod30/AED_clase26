from accessLevel.classA import A
from accessLevel.classC import C
from ClassB import B

a: A = A()
b: B = B()
c: C = C()
print(a._protected_attrib)
print(f"Public attribute in instance a {a.public_attrib} and in instance b {b.public_attrib}")
print(f"Public class attribute {a.public_class_attribute}")
A.public_class_attribute = "changed for all instances"
print(f"Public class attribute in a instance {a.public_class_attribute} and in b instance {b.public_class_attribute}")
print(a)
print(b)
b.print_public()
b.print_protected()
# b.print_private() # <- runtime error: __private_attrib is not defined in class B
c.print_public()
c.print_protected()
# print (a.__private_attrib) # <-- runtime error: __private_attrib is a private attribute in class A
