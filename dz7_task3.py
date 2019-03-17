# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.

import random

# Поиск медианы без сортировки

def find_median(array):
    for item in array:
        less_item = 0
        more_item = 0
        eq_item = 0
        for i in array:
            if i < item:
                less_item += 1
            if i > item:
                more_item += 1
            if i == item:
                eq_item += 1
        if abs(less_item - more_item) < eq_item:
            return int(item)

# Поиск медианы с сортировкой. Использую для контроля

def control_find_median(array):
    return int(sorted(array)[len(array) // 2])

MIN_NUM = 0
MAX_NUM = 10

m = int(input('Введите m: '))
array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(2 * m + 1)]

median = find_median(array)

print(f"Исходный массив: \n", *array)
print(f"Отсортированный массив  \n", *sorted(array))
print(f'Медиана = {median}')

if control_find_median(array) - median != 0:
    print('Ошибка! Разные методы поиска медианы дают разное значение.')
