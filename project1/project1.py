print('Скажите ФИО')
fullname = input()
print('Скажите номер группы с указанием подгруппы')
group = input()
print('Скажите год рождения')
year = int(input())
print('Скажите дату первого занятия')
date = input()

age = 2025 - year
print(age)

print(f'Здравствуйте! Я, {fullname}, студент из группы {group}')

a4 = 2.7 / 2
b4 = 2 / 4 - 1
c4 = 2 // 4 - 1
d4 = (2 + 5) % 3
e4 = 2 + 5 % 3
f4 = 3 * 4 // 6
g4 = 3 * (4 // 6)
h4 = 3 * 2 ** 2
i4 = 3 ** 2 * 2
print(a4, b4, c4, d4, e4, f4, g4, h4, i4)

a5 = -2 ** 2
b5 = 2 ** -2
c5 = -2 ** -2
d5 = 2 ** 2 ** 3
e5 = 2 ** 3 ** 2
f5 = -2 ** 3 ** 2
g5 = (-2) ** 3 ** 2
h5 = (-2) ** 2 ** 3
print(a5, b5, c5, d5, e5, f5, g5, h5)

a6 = not 1 < 2 or 4 > 2
b6 = not (1 < 2 or 4 > 2)
c6 = 1 < 2 or 4 > 2
d6 = 4 > 2 or 10/0 == 0
e6 = not 0 < 1
f6 = 1 and 2
g6 = 0 and 1
h6 = 1 or 0
print(a6, b6, c6, d6, e6, f6, g6, h6)
