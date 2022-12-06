'''
Дан текст в котором встречаются имена и следующие за ними фамилии.
Нужно получить список фамилий (last name) людей которых зовут Иван.
Если на английском, то Michael)

const inputText = "Michael, how are you? - Cool, how
is John Williamns and Michael Jordan? I don't know but Michael Johnson is fine.
Michael do you still score points
with LeBron James, Michael Green AKA Star and Michael Wood?"

Должно выдать ["Jordan", "Johnson", "Green", "Wood"]
'''

import re


text = """Michael, how are you? - Cool, how
        is John Williamns and Michael Jordan? I don't know but Michael Johnson is fine.
        Michael do you still score points
        with LeBron James, Michael Green AKA Star and Michael Wood?"""

match = re.findall(r'Michael [A-Z]\w+', text)
new = []
for i in match:
    i = i.split()
    new.append(i[1])
print(new)
