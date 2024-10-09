#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

dot_A = int(input('Введите координату точки A: '))
dot_B = int(input('Введите координату точки B: '))
dot_C = int(input('Введите координату точки C: '))

lenght_AC = abs(dot_C - dot_A)
lenght_BC = abs(dot_C - dot_B)

print(f'''
Длина отрезка AC: {lenght_AC}.
Длина отрезка BC: {lenght_BC}.
Сумма длин отрезков AC и BC: {lenght_AC + lenght_BC}''')