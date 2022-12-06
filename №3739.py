'''
Задача №3739. Первое и последнее вхождение

Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего
появления. Если буква f в данной строке не встречается, ничего не выводите.

При решении этой задачи нельзя использовать метод count и циклы.
'''
import re


string = 'comfortable office'

match = re.findall(r'f', string)
if len(match) > 1:
    first = string.find('f')
    last = string.rfind('f')
    print(first, last)
elif len(match) == 1:
    print(string.find('f'))
