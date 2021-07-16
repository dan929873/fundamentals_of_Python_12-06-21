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

   def wrapper(*args, **kwargs):
       # print name fun
       print(f'{func.__name__} {args}')
       # print type args
       for index in range(len(args)):
           print(f"{type(args[index])}, ", end='')
       # print kwargs
       if len(kwargs):
           print("\nkwargs: ", end='')
           for pet, name in kwargs.items():
               print(f"{type(pet)}: {type(name)}")
       # call fun
       markup = func(*args)
       print(f'\nтип значения функции: {type(markup)}')

       return markup

   return wrapper


@type_logger
def calc_mult(x, b):
   return x * b


def printScores(student, *args, **kwargs):
   print(f"Student Name: {student}")
   for score in args:
       print(score)
   for pet,name in kwargs.items():
      print(f"{pet}: {name}")


printScores = type_logger(printScores)
printScores("Jonathan",100, 95, 88, 92, 99, fish=["Larry", "Curly", "Moe"])

username_f = calc_mult(3, 5.6)
print(username_f)
