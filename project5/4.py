lst = []
n = int(input(f'Введите количество элементов списка: '))
for i in range(n):
    lst.append(int(input(f'Введите элемент списка: ')))
print(lst)

minimal = min(lst)
maximal = max(lst)
average = sum(lst) / len(lst)
print(f'Минимальное: {minimal}\nМаксимальное: {maximal}\nСреднее арифметическое: {average}\n')