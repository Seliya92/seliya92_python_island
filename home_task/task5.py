#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

print(f'''
Сумма чисел = {number_1 + number_2}
Разность чисел = {number_1 - number_2}
Частность чисел = {number_1 / number_2}
Произведение чисел = {number_1 * number_2}
Результат целочисленного деления = {number_1 // number_2}
Остаток от деления первого чиссла на второе = {number_1 % number_2}
Первое число в степени второго = {number_1 ** number_2}''')