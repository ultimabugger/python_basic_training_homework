my_el_list = [3, 45, 37, 45, 23, 6, 7, 7, 7, 93, 45, 45]
new_list = [el for el in my_el_list if my_el_list.count(el) == 1]
print(new_list)