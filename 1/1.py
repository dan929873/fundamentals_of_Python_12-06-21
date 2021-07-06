# 1. Написать скрипт, создающий стартер (заготовку) для проекта со
# следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
# (как быть?); как лучше хранить конфигурацию этого стартера,
# чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных
# папках и файлах (добавлять детали)?


import os

my_name_dir = {'my_project': {'settings': None, 'mainapp': None, 'adminapp': None, 'authapp': None}}

def print_dir(my_dir):
    for key in my_dir.keys():
        print(key, '->', my_dir[key])
        if isinstance(my_dir[key], dict):
            print_dir(my_dir[key])


    # print(val)

print_dir(my_name_dir)

