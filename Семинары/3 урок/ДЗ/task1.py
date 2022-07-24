""" Задайте список. Напишите программу, которая определит,
 присутствует ли в заданном списке строк некое число. """

from ast import Num
from operator import indexOf


ls=['qwe', 'ryh','dxhh',55,'zhrhzthx',64363,'zgxvrb',97]
def find_num(ls):
    ls1=[]
    for i in ls:
        print(i, end=' ')
        if type(i)==int:
            ls1.append(indexOf(ls,i))
    print(f'Индексы цифр - {ls1}',end='')
find_num(ls)
