#todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
start_number = input('Введите число, удовлетворяющее условию: "Данное четырехзначное число читается одинаково слева направо и справа налево": ')
end_number = start_number[::-1]
print(start_number == end_number)