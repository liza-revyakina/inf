import random

n = int(input("Введите количество элементов в списке: "))
lst = [random.randint(-2, 2) for i in range(0, n)]
print(lst)

zero = lst.count(0)
print(f'Ноль встречается {zero} раз')

i = 0
while i < len(lst):
    if lst[i] == 0:
        if i < len(lst) - 1 and lst[i + 1] == 0:
            del lst[i:i + 2]
            continue
        elif lst[i - 1] + lst[i - 2] == 0:
            index = i - 2
            while lst[index] + lst[index - 1] == 0:
                index -= index - 1
            lst[i] = lst[index] + lst[index - 1]
        else:
            lst[i] = lst[i - 1] + lst[i - 2]
    i += 1

print(lst)

positive = []
negative = []
for i in lst:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)

print(f'Положительные числа: {positive}\nОтрицательные числа: {negative}')