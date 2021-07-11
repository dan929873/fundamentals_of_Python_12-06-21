# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
# верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os


my_static =  { '100': 0, "1000": 0, "10000": 0, "100000": 0}


def count_file(my_dir):
    for file in os.listdir(my_dir):
        if os.path.isdir(f"{my_dir}/{file}") :
            count_file(f"{my_dir}/{file}")
        else:
            size_file = os.path.getsize(f"{my_dir}/{file}")
            if 100 >= size_file:
                my_static["100"] += 1
                continue
            if 1000 >= size_file > 100:
                my_static["1000"] += 1
                continue
            if 10000 >= size_file > 1000:
                my_static["10000"] += 1
                continue
            if size_file > 10000:
                my_static["100000"] += 1
                continue




count_file("../../fundamentals_of_Python_12-06-21")

print(my_static)