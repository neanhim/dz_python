
# Задание 7
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
#

import random

MIN_LIMIT = 0
MAX_LIMIT = 100
SIZE = 10

array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

min_elem = MAX_LIMIT
min_elem_index = 0
max_elem = MIN_LIMIT
max_elem_index = 0

for item in enumerate(array):
    if item[1] <= min_elem:
        min_elem = item[1]
        min_elem_index = item[0]
    if item[1] >= max_elem:
        max_elem = item[1]
        max_elem_index = item[0]

print("Минимальное значение\t ", min_elem)
print("Максимальное значение\t ", max_elem)

if max_elem_index > min_elem_index:
    a, b = min_elem_index, max_elem_index
else:
    b, a = min_elem_index, max_elem_index

sum = 0
for index in range(a + 1, b):
    sum += array[index]

print(f"Cумма элементов, находящихся между минимальным и максимальным элементами {sum}")
