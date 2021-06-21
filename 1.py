# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык. Например:
#
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

def num_translate(my_str):
    """the function inpput string 'one' - 'ten' and print translate to russia number or return None if data not string 'one' - 'ten'"""

    eng_num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    rus_num = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}

    for key, val in eng_num.items():
        if (val == my_str):
            print(rus_num[key])
    else:
        return None


num_translate('one')
