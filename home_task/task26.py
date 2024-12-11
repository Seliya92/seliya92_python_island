# #todo Задача 1. Чтение матрицы, load_matrix(filename)
# # Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# с
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

import csv
def load_matrix(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        rows = [[int(num) for num in row] for row in reader]

    num_cols = len(rows[0]) if rows else 0
    if all(len(row) == num_cols for row in rows):
        return print(rows)
    else:
        return False
load_matrix('matrix.csv')