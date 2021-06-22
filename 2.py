# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы. Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def thesaurus(*args):
    my_dict = {}

    for index in range(len(args)):
        if isinstance(args[index], str):                        # проверка на строку значения подаваемого списка
            first_word = args[index][0]
            my_dict.setdefault(first_word, []).append(args[index])
        else:
            print(f"имя под номером {index + 1} не строка")
    return my_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", 2))
