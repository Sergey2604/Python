""" Вычислить результат деления двух чисел c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ """


"""from cmath import pi
d = float(input('Введите необходимую точность вычисления: '))

def find_num(d):
    print(pi)
    counted = 0
    while d < 1:
        d = d*10
        counted += 1
    print(counted)
    num = pi
    print(num)
    num = round(num, counted)
    print(num)
    print(num)


find_num(d)
 """
a = float(input('Введите число 1: '))
b = float(input('Введите число 1: '))
d = float(input('Введите необходимую точность вычисления: '))


def find_num(a, b, d):
    counted = 0
    while d < 1:
        d = d*10
        counted += 1
    c = round(a/b, counted)
    print(c)


find_num(a, b, d)
