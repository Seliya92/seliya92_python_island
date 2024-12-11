#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = "abcdefghijklmnopqrstuvwxyz "

str = input("Введите текст: ")
list = str.split(" ")
new_str = ""
i = 0
while i < len(list):
    l = alphabet[int(list[i]) - 1] if list[i].isdigit() else list[i]
    i += 1
    new_str = new_str + l

print(new_str)