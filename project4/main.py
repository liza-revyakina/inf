test_list = input("Введите значения через пробел: ").split()
a = []
for each in test_list:
    a.append(each)
print(len(a))
a.reverse()
print(a)

