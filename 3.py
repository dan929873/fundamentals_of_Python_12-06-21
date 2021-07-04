# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
# что объём данных в файлах во много раз меньше объема ОЗУ.


def my_script(name, hobby):
    with open(name, 'r') as content_f:
        full_name = content_f.read().split('\n')
    with open(hobby, 'r') as content_f:
        hobby = content_f.read().split('\n')

    if len(full_name) == len(hobby):
        with open("result_dict.txt", 'w') as result_dict:
            result_dict.write(str({full_name[index_fn]: hobby[index_fn] for index_fn in range(len(full_name))}))
    elif len(full_name) > len(hobby):
        for index in range(len(full_name) - len(hobby)):
            hobby.append('None')
        with open("result_dict.txt", 'w') as result_dict:
            result_dict.write(str({full_name[index_fn]: hobby[index_fn] for index_fn in range(len(full_name))}))
    else:
        return 1


print(my_script("full_name", "hobby"))
