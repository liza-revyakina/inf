n = int(input('Введите число: '))
if n < 0:
    print('Число отрицательное')
else:
    print('Число положительное')
if n % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
if x % y == 0:
    print('Первое число делится без остатка на второе')
else:
    print('Первое число не делится без остатка на второе')

number = int(input('Введите число: '))
for numbers in range(1, 301):
    if numbers % number == 0:
        print(numbers)
    else:
        continue

year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0:
    print('Год високосный')
elif year % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')

year = int(input('Введите год: '))
animals = ['дракон', 'змея', 'лошадь', 'коза', 'обезьяна', 'петух', 'собака', 'свинья', 'крыса', 'бык', 'тигр', 'кролик']
print(animals[(year - 2000) % 12])
