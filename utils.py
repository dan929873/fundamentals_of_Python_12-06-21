# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils


def currency_rates(str_name):

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    my_list_name = content.split('<CharCode>')
    my_list_value = content.split('<Value>')
    my_dict = {}
    for iter in range(len(my_list_name)):
        if iter != 0:
            list_name = str(my_list_name[iter][:3])
            list_val = float(my_list_value[iter][:8].replace(',','.').replace('<',''))

            my_dict.setdefault(list_name, list_val)

    if str_name in my_dict:
        return my_dict[str_name]
    else:
        return None



if __name__ == '__main__':

    print(currency_rates("KGS"))
