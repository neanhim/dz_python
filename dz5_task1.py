# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import deque

companies = []

n = int(input("Введите количество предприятий\n"))

total_profit = 0
average_profit_all = 0

for i in range(n):
    comp_name_temp = str(input("Введите название организации\n"))
    profits_temp = deque([int(input(f"Введите прибыль за {_}-й квартал\n")) for _ in range(1,5)], maxlen=4)
    average_profit_temp = sum(profits_temp) / 4
    companies.append({"comp_name": comp_name_temp, "profits": profits_temp, "average_profit": average_profit_temp})
    average_profit_all += average_profit_temp/n

print(f"Средняя прибыль по всем компаниям: {average_profit_all}")

print("Организации, чья прибыль выше среднего:")
for i in companies:
    if i["average_profit"] > average_profit_all:
        print(i["comp_name"])

print("Организации, чья прибыль ниже среднего:")
for i in companies:
    if i["average_profit"] < average_profit_all:
        print(i["comp_name"])