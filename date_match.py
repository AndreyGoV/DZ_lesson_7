'''
RE для определения, есть ли в строке хотя бы одна дата в формате [mm-dd].
Две цифры для месяца, тире и две цифры для дня. Окружены квадратными скобками.)
Работаем только с невисокосными годами. Число дней в месяцах учитывается!

1. January - 31 days
2. February - 28 days (leap years are ignored)
3. March - 31 days
4. April - 30 days
5. May - 31 days
6. June - 30 days
7. July - 31 days
8. August - 31 days
9. September - 30 days
10. October - 31 days
11. November - 30 days
12. December - 31 days

Примеры работы:

"[01-23]" // January 23rd is a valid date
"[02-31]" // February 31st is an invalid date
"[02-16]" // valid
"[ 6-03]" // invalid format
"ignored [08-11] ignored" // valid
"[3] [12-04] [09-tenth]" // December 4th is a valid date
'''

import re


calendar = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
}


def date_format_check(string):
    match = re.findall(r'[\[][0-1][0-9]-[0-3][0-9][]]', string)
    if len(match) == 0:
        return 'В данной строке отсутствует дата в корректном формате'
    elif len(match) >= 1:
        for i in match:
            cor = re.findall(r'\d+', i)
            month = cor[0]
            date = int(cor[1])
            if month in calendar:
                k = calendar[month]
                if date in range(1, k + 1):
                    return 'В данной строке присутствует дата'
                else:
                    return 'В данной строке отсутствует дата в корректном формате'
            else:
                return 'В данной строке отсутствует дата в корректном формате'


print(date_format_check("[3] [12-04] [09-tenth]"))
