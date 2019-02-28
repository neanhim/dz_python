
# Задание 9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#

import random

def PrintMatrix(matrix):
    for row in matrix:
        for item in row:
            print(f"{item:>5}",  end="")
        print()
    print()

MIN_LIMIT = 1
MAX_LIMIT = 10
NUM_ROWS = 5
NUM_COLUMNS = 5

matrix = [[random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(NUM_COLUMNS)] for __ in range(NUM_ROWS)]
PrintMatrix(matrix)

min_elements = [MAX_LIMIT for _ in range(NUM_COLUMNS)]
for row in matrix:
    for index in range(NUM_COLUMNS):
        if min_elements[index] > row[index]:
            min_elements[index] = row[index]

max_element = MIN_LIMIT
for item in min_elements:
    if item > max_element:
        max_element = item
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы - {max_element}")


