# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sort(array):
    n = 1
    while n < len(array):
        ch = 0
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                ch = 1
        n += 1
        if ch == 0:
            break

MIN_NUM = -100
MAX_NUM = 99
NUM_ELEMENTS = 25

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(NUM_ELEMENTS)]

print(f"Исходный массив: \n", *array)

bubble_sort(array)

print(f"Отсортированный массив: \n", *array)

