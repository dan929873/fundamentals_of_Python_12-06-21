# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

def my_gen(n):
    if not isinstance(n, int):
        return None
    my_gen = (el for el in range(1, n+1) if el % 2 != 0)
    return my_gen

mg = my_gen(1000)
print(type(mg))
print(list(mg))
