# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.

alphabet = "abcdefghijklmnopqrstuvwxyz"
text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
i = 0
while i < len(alphabet):
    new_text = ""
    for l in text:
        if l in alphabet:
            tmp_index = alphabet.index(l) + i if (alphabet.index(l) + i) < 25 else alphabet.index(l) + i - 26
            new_l = alphabet[tmp_index]
        else:
            new_l = l
        new_text = new_text + new_l
    print(i)
    print(new_text)
    i +=1
