def sep_float(number):
    temp = number % 1
    print(round(temp // 0.1))


number = input('Введите число: ')
sep_float(number)
