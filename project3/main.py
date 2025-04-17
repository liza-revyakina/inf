line = input("Введите строку: ")
print(f"Длина строки {len(line)}, последний символ строки {line[-1]}")

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
if word1[0] == word2[0]:
    print("Первые буквы совпадают")
else:
    print("Первые буквы не совпадают")

word = input("Введите слово: ")
letter = word[-1]
if letter == 'ь':
    print(f"Последняя буква {letter}, предпоследняя буква {word[-2]}")
else:
    print(f"Последняя буква {letter}")

new_line = input("Введите строку не менее шести символов: ")
first = new_line[:3]
last = new_line[-3:]
print(first + last)

text = input("Введите строку: ")
sub = input("Введите подстроку: ")
print(text.count(sub))

print(text.upper())
print(text.title())
new_letter = input("Введите букву: ")
print(text.replace(new_letter, new_letter.upper()))

print(text[::-1])

name = input("Введите фамилию, имя, отчество: ").split()
print(f'{name[0][0]} {name[1][0]} {name[2][0]}')

university = input('Введите название университета: ')
print(university.split()[0][0] + university.split()[1][0].upper() + university.split()[2][0].upper())
print(university.split()[0][:3] + university.split()[1][0].upper() + university.split()[2][0].upper())

