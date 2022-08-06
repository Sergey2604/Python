S = input("Введите текст: ")


def coding(tekst):
    count = 1
    A = ''
    for i in range(len(tekst)-1):
        if tekst[i] == tekst[i+1]:
            count += 1
        else:
            A = A + str(count) + tekst[i]
            count = 1
    return A


def decoding(tekst):
    number = ''
    A = ''
    for i in range(len(tekst)):
        if not tekst[i].isalpha():
            number += tekst[i]
        else:
            A = A + tekst[i] * int(number)
            number = ''
    return A


print(f"Кодирование: {coding(S)}")
print(f"Декодирование: {decoding(coding(S))}")
