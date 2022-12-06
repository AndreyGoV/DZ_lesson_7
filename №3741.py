'''
Задача №3741. Удаление фрагмента

Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки
первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
'''

# Первый способ
import re

string = 'In the hole in the ground there lived a hobbit'

split = re.split(r'h.*h', string)
result = ''.join(split)
print(result)

# Второй способ
first = string.find('h')
last = string.rfind('h')

result = []
result.append(string[:first])
result.append(string[last + 1:])
print(''.join(result))
