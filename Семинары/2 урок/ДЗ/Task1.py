""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
 """
number=input('Введите вещественное или целое число: ')

def summary(num):
    sum=0
    list=[]
    i=0
    for j in number:
        if j=='.' or j==',':
            j=0
        list.append(int(j))
        sum=sum+list[i]
        i+=+1
    print(f'Сумма цифр введенного числа = {sum}')
    return sum
summary(number)