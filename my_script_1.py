# бесконечный итератор, генерирующий целые числа,
# начиная с указанного

"""from itertools import count


def num_func(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
    num_func(start_num=int(input("Наберите стартовое число: ")), stop_num=int(input("Наберите стоп число: ")))"""


# бесконечный итератор, повторяющий элементы
# некоторого списка, определенного заранее.

from itertools import cycle


def cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


cycle_func(my_list=[1, 2, 3], iteration=int(input("Введите итерацию")))
