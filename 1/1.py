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
import errno
import os
import yaml

my_name_dir = {'my_project': {'settings': None, 'mainapp': None, 'adminapp': None, 'authapp': None}}

# a_yaml_file = open(" config.yaml")
# my_name_dir = yaml.safe_load(a_yaml_file)


def print_dir(create_dir, my_dir = None):

    if my_dir != None:
        os.chdir(str(my_dir))
    for key in create_dir.keys():
        if not os.path.isdir(str(key)):
            os.mkdir(str(key))
        if create_dir[key] is not None:
            print_dir(create_dir[key], key)






print_dir(my_name_dir)

