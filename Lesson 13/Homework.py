from threading import Thread
from random import randint


list_of_numbers = []


def preparing_list():
    for i in range(10000):
        i = randint(1, 100)
        list_of_numbers.append(i)

    print(list_of_numbers)
    return list_of_numbers


def amount_calculation():
    amount = sum(list_of_numbers)
    print(f"Сумма элементов в списке = {amount}")
    return amount


def mean_calculation():
    mean = sum(list_of_numbers)/len(list_of_numbers)
    print(f"\nСреднее аримфмитическое значение = {mean}")
    return mean


t1 = Thread(target=preparing_list)
t2 = Thread(target=amount_calculation)
t3 = Thread(target=mean_calculation)

t1.start()
t1.join()
t2.start()
t3.start()