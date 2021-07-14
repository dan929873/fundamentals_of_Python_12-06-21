# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
   cache = {}

   def wrapper(*args, **kwargs):
       print('args', args)
       print('kwargs', kwargs)
       markup = func(*args, **kwargs)
       print(markup)
       return markup

   return tag_wrapper


@type_logger
def calc_cube(x):
   return x ** 3


username_f = render_input('username')
print(render_input)
