from functools import reduce


def my_func_list(prev_el, el):
    return prev_el * el


print(f"Четные значения {[el for el in range(99, 1001) if el % 2 == 0]}")
print(f"Результат перемножения {reduce(my_func_list, [el for el in range(99, 1001) if el % 2 == 0])}")
