""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. """

from operator import countOf

with open('file1.txt', 'r') as file:
    string1 = file.read()
    file.close
print(string1)

def coding(cod):
    new_code = f'{countOf(cod, cod[0])}{cod[0]}'
    previously = cod[0]
    for i in range(len(cod) - 1):
        if cod[i] != previously:
            new_code = f'{new_code}{countOf(cod, cod[i])}{cod[i]}'
        previously = cod[i]
    with open('coding.txt', 'a') as file:
        file.write(f'{new_code}\n')
        file.close()
    return new_code


def decoding(cod):
    new_code1 = ''
    symbol_str = ''

    for i in range(len(cod)):
        # symbol_int = int(symbol_str)
        if not cod[i].isalpha():
            symbol_str = f'{symbol_str}{cod[i]}'
        elif cod[i].isalpha():
            new_code1 = f'{new_code1}{cod[i] * int(symbol_str)}'
            symbol_str = ''
    print(f'decoding   {new_code1}')
    with open('decoding.txt','a') as file:
        file.write(f'{new_code1}\n')
        file.close()
    return new_code1


decoding(coding(string1))
