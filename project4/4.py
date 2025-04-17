lst = []
n = int(input(f'Введите количество элементов списка: '))
for i in range(n):
    lst.append(int(input(f'Введите элемент списка: ')))
result = []
for i in lst:
    if i not in result:
        result.append(i)
print(lst)
print(f'Без дубликатов: {result}')
