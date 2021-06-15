# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.


def sec(num):
    year = num / 31556926
    if (year > 1) :
        year = num // 31556926
        num = num - (year * 31556926)
        print(f"{year} г. ", end='')
    day = num / 86400
    if (day > 1):
        day = num // 86400
        num = num - (day * 86400)
        print(f"{day} д. ", end='')
    hour = num / 3600
    if (hour > 1):
        hour = num // 3600
        num = num - (hour * 3600)
        print(f"{hour} ч. ", end='')
    min = num / 60
    if (min > 1):
        min = num // 60
        num = num - (min * 60)
        print(f"{min} м. ", end='')
    print(f"{num} с.")

if __name__ == '__main__':
    sec(89999999)



