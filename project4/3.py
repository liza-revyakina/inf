a = []
p = []
k = 0
for i in range(3):
    a.append(int(input(f'Введите элемент списка: ')))
print(a)
for i in range(3):
    n = 1
    for m in range(3):
        if m != i:
            n *= a[m]
    p.append(n)
print(p)
