# #Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

n = abs(int(input('Введите число N: ')))

position_one = int(input('Введите первое число: '))
position_two = int(input('Введите второе число: '))

starting_position = 1
ending_position = n * 2 + 1
positions_range = range(starting_position, ending_position + 1)

if position_one not in positions_range or position_two not in positions_range:
    print('Некорректные позиции')
else:
    seq = []
    for i in range(-n, n + 1):
        seq.append(i)
    print(f"Произведение элементов {seq}")
    print(
        f"Находящихся на позициях {position_one} и {position_two} равна {seq[position_one - 1] * seq[position_two - 1]}")
