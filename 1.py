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
    
    if (my_str == 'one'):
        print('один')
    if (my_str == 'two'):
        print('два')
    if (my_str == 'three'):
        print('три')
    if (my_str == 'four'):
        print('четыре')
    if (my_str == 'five'):
        print('пять')
    if (my_str == 'six'):
        print('шесть')
    if (my_str == 'seven'):
        print('семь')
    if (my_str == 'eight'):
        print('восемь')
    if (my_str == 'nine'):
        print('девять')
    if (my_str == 'ten'):
        print('десять')
    else:
        return None


num_translate('one')
