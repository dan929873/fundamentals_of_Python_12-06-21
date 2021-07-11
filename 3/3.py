# 3. Создать структуру файлов и папок, как написано в задании 3 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os
from shutil import copyfile


def return_directory(my_dir, name_dir_where_save = 'templates'):

    index_dir_find = my_dir.find(name_dir_where_save) #the need for not parsing 'name_dir_where_save'
    len_name_dir = len(my_dir.split('/')[0])

    for file in os.listdir(my_dir):
        if os.path.isdir(f"{my_dir}/{file}") and (index_dir_find == -1 or index_dir_find > len_name_dir):
            return_directory(f"{my_dir}/{file}", name_dir_where_save)
        else:
            if file.endswith(".html"):
                if not os.path.isdir(f"my_project/{name_dir_where_save}/"):
                    os.mkdir(f"my_project/{name_dir_where_save}/")
                dir_source = my_dir.split("/")[1]
                if not os.path.isdir(f"my_project/{name_dir_where_save}/{dir_source}"):
                    os.mkdir(f"my_project/{name_dir_where_save}/{dir_source}")
                copyfile(f"{my_dir}/{file}", f'my_project/{name_dir_where_save}/{dir_source}/{file}')



return_directory("my_project")