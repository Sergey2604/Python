# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

n = int(input('Введите натуральное число: '))


def find_num(n):
    ls = []
    count = 1
    while count < n:
        if n % count == 0:
            ls.append(count)
        count += 1
    print(f'Простые множители числа {n} - {ls}')


find_num(n)
