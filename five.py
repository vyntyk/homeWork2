# #Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

n = int(input("Введите число элементов в списке: "))
arr = [random.randint(-100, 100) for i in range(n)]
print(arr)

def mix(arr):
    l = len(arr)
    indices = []
    new_arr = []
    i = 0
    while (i < l):
        j = random.randint(0, l - 1)
        if j not in indices:
            indices.append(j)
            new_arr.append(arr[j])
            i += 1
    return new_arr

print(mix(arr))
