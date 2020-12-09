my_list = [100, 50, 63, 79, 7, 19, 39, 543, 67, 97]
new_list = [num for num in my_list if num > my_list[my_list.index(num) - 1]]
print(f"Старый список {my_list}")
print(f"Новый список {new_list}")