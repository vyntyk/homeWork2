# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

str_num = input('Введите вещественное число: ')

n = len(str_num)
num = abs(int(float(str_num) * 10 ** n))
digits_sum = 0

while num >= 10:
    digits_sum += num % 10
    num //= 10

digits_sum += num
print(f"Сумма цифр в числе: {'{:.0f}'.format(digits_sum)}")
