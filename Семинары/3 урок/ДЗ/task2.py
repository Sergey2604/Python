""" Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:

список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1 """

from itertools import count


ls = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]


def find_second(ls):
    find = input('Введите строку для поиска: ')
    i = 0
    ls1 = []
    while i < len(ls):
        counted = 0
        if ls[i] == find:
            ls1.append(i)
            counted += 1
        i += 1
    if ls.count(find) >= 2:
        print(
            f'Количество вхождений {find} - {ls.count(find)}, второе вхождение - {ls1[1]}')
    else:
        print(f'Вхождений {find} меньше двух')


find_second(ls)
