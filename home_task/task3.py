# todo: Данные две переменные:
# age = 36.6
# temperature = 25
# Нужно обменять значения переменных местами. В итого age
# должен равнятся 25 а temperature – 36.6:

age = 36.6
temperature = 25
x = age
age = temperature
temperature = x
print(f"Age = {age}")
print(f"Temperature = {temperature}")