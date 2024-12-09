# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
#
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = ""
with open("message.txt", "r") as fp:
    rows = fp.readlines()
for row in rows:
    # print(row)
    row_index = rows.index(row) + 1
    # print(row_index)
    tmp_row = row.lower()
    # print(tmp_row)
    # print(len(tmp_row))
    i = 0
    while i < len(tmp_row):
        l = tmp_row[i]
        if l in alphabet:
            tmp_index = alphabet.index(l) + row_index if (alphabet.index(l) + row_index) < 32 else alphabet.index(l) + row_index - 33
            new_l = alphabet[tmp_index] if row[i].islower() else alphabet[tmp_index].upper()
        else:
            new_l = row[i]
        text = text + new_l
        # print(row[i], new_l)
        i +=1

f = open("new_message.txt", "w+t")
f.write(text)
f.close()






