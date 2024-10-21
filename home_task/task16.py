# # todo: База данных пользователя.
# # Задан массив объектов пользователя
#
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введенного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Введите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"



def init():
    users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
             {'login': 'Ivan',  'age': 10, 'group': "guest"},
             {'login': 'Dasha', 'age': 30, 'group': "master"},
             {'login': 'Fedor', 'age': 13, 'group': "guest"}]
    return users


def choose_type_sorter():
    while True:
        a = int(input("""Выберите тип сортировки:
    1. По возрасту
    2. По первой букве
    3. По группе
Тип сортировки: """))
        if a > 0 and a < 4 :
                break
        else:
                print("Некорректный тип сортировки.")
    return a
def print_user(user):
    print(f'Пользователь: {user['login']} возраст {user['age']} {'года' if int(user['age']) % 20 < 5 and int(user['age']) % 10 > 0 else 'лет'} , группа {user['group']}')

def sorter(type,users):
    match type:
        case 1:
            age = int(input("Введите возраст:"))
            for user in users:
                if int(user['age']) >= age:
                    print_user(user)
        case 2:
            letter = input("Введите первую буквву логина:")
            for user in users:
                if letter.upper() == user['login'][0]:
                    print_user(user)
        case 3:
            group = input("Введите группу:")
            for user in users:
                if group == user['group']:
                    print_user(user)

sorter(choose_type_sorter(), init())






