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
mailk = "someone@geekbrainsru"

patern_name = r"^\w+"
patern_domain = r"(?<=@)\w+.\w+"

def email_parse(mail):

    my_res = {}
    assert re.findall(patern_name, mail)
    assert re.findall(patern_domain, mail)
    # assert patern_name.findall(mail), patern_domain.findall(mail)

def email_parse(email_address):
    parsed = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))

print(email_parse(mail))

print( re.findall(r"(^\w+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", mail))
