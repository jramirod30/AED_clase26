from typing import Any

data_list: list = []
data_list.append(3)
data_list.append("Hello")
data_list.append(True)
for inf in data_list:
    print(f" data: {inf} type is: {type(inf)}")
data_list2: list[int] = []
data_list2.append(3)
data_list2.append("Hello")
data_list2.append(False)
for inf in data_list2:
    print(f" data: {inf} type is: {type(inf)}")
data_int: int = 12
data_bool: bool = False
print(f"data type data_bool {type(data_bool)}")
data_bool = data_int
print(f"data type data_bool {type(data_bool)}")



def func(param: Any) -> None:
    print(type(param))
