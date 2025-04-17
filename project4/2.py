list1 = input("Введите первый список: ").split()
lst1 = []
for num in list1:
    lst1.append(int(num))
list2 = input("Введите второй список: ").split()
lst2 = []
for num in list2:
    lst2.append(int(num))
lst3 = []
for i in range(len(lst1)):
    lst3.append(lst1[i] + lst2[i])

print(lst3)
