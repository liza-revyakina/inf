new_line = input("Введите строку: ")
n = int(input("Введите количество первых символов: "))
m = int(input("Введите количество вторых символов: "))
first = new_line[:n]
last = new_line[-m:]
print(first + last)