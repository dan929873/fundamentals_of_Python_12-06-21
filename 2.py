# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
#
#     Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
#     так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#     К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#     Внимание: новый список не создавать!!!


def cub():
    arr = [i ** 3 for i in range(1, 1001, 2)]
    my_summ = 0

    for n in arr:
        summ = 0
        for num in str(n):
            summ += int(num)
        if (summ % 7) == 0:
            my_summ += n
    print(my_summ)
    my_summ = 0
    for n in arr:
        n += 17
        summ = 0
        for num in str(n):
            summ += int(num)
        if (summ % 7) == 0:
            my_summ += n
    print(my_summ)

if __name__ == '__main__':

    cub()
