# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?


import re


mail = "someone@geekbrains.ru"
mail_er = "someone@geekbrainsru"

def email_parse(email_address):
    patern = r"(^\w+)@((?<=@)[\w]+\.\w+)"
    result = re.findall(patern, email_address)
    if not result:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], result[0]))

print(email_parse(mail_er))

