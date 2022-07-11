x=int(input('Введите координаты числа X: '))
y=int(input('Введите координаты числа Y: '))
def coordinates(x,y):
    if x>0 and y>0:
        print('Вы ввели координаты 1 четверти')
    elif x>0 and y<0:
        print('Вы ввели координаты 2 четверти')
    elif x<0 and y<0:
        print('Вы ввели координаты 3 четверти')
    else:
        print('Вы ввели координаты 4 четверти')
coordinates(x,y)