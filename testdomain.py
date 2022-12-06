'''
Написать RE которая мэтчит адреса эл. почты
только с конкретным именем домена (testdomain):
 ****@testdomain.com - valid
 ****@anotherdomain.com - not valid
'''

import re


mail_list = '''
Ivanov@yandex.ru
Petrov@testdomain.com
Sidorov@testdomain.ru
Letov@testdomain.com
Putin@gmail.com
'''

match = re.findall(r'\w+@testdomain.com', mail_list)
print(match)
