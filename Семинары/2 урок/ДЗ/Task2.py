""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

n=int(input('Введите число: '))

def multi(n):
    ls=[]
    last=1
    for i in range(n):
        ls.append(i+1)
    print(f'ls: {ls}')
    for i in range(n):
        ls[i]=last*ls[i]
        last=ls[i]
    print(f'ls new: {ls}')
    return ls
multi(n)
