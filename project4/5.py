strng = input(f'Введите строку с целыми числами: ')
number = strng.split()
lst = []
for num in number:
    lst.append(int(num))
print(lst)
ascending = sorted(lst)
descending = sorted(lst, reverse=True)
print(f'По возрастанию: {ascending}')
print(f'По убыванию: {descending}')

