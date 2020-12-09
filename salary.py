from sys import argv

file_name, worked_hour, salary, prize = argv

sum_total = float(worked_hour) * float(salary) + float(prize)
print(f"Зарплата сотрудника составляет {sum_total}")
