# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from requests import get, utils

response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
content = content.split('\n')
result = []
mystr = 0 #для подсччета строк и проверки на потерю данных
for iter in range(len(content)):
    my_list = list()
    x = content[iter][0:content[iter].find(' - - ')]
    my_list.append(x)
    my_list.append(content[iter][content[iter].find('] "')+3:content[iter].find(' /')])
    my_list.append(content[iter][content[iter].find(' /')+2:content[iter].find(' HTTP')])
    result.append(tuple(my_list))

    if (len(my_list)>2):
        mystr += 1

print(mystr, len(content))
print(result[0: 10])
