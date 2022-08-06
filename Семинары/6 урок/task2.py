""" 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты 
группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:

aaaabbcaa
Sample Output 1:

a4b2c1a2
Sample Input 2:

abc
Sample Output 2:

a1b1c1 """

code = input('Введите строку, состоящую только из букв')
ls_decoding = ''


def Coding(code):

    previous = code[0]
    for i in code:
        count = 1
        if i == previous:
            count += 1
        ls_decoding = ls_decoding+f'{i}{count}'
        previous = i
    print(ls_decoding)
    return ls_decoding


def decoding(ls_deccoding):
    number = ''
    A = ''
    for i in range(len(ls_deccoding)):
        if not ls_deccoding[i].isalpha():
            number += ls_deccoding[i]
        else:
            A = A + ls_deccoding[i] * int(number)
            number = ''
    return A


Coding(code)
decoding(ls_decoding)
