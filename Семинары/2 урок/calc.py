""" Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
 """

firstNum=str(input('Введите первое число'))
secondNum=str(input('Введите второе число'))
operation=str(input('Введите операцию: '))

def oper (a,b):
    if operation=='/' and secondNum=='0':
        print('Деление на 0!')
    elif operation== '+':
        print(float(a)+float(b))
    elif operation=='-':
        print(float(a)-float(b))
    elif operation=='*':
        print(float(a)*float(b))
    elif operation=='/':
        print(float(a)/float(b))
    elif operation=='mod':
        print(float(a)%float(b))
    elif operation=='pow':
        print(pow(float(a),float(b)))
    elif operation=='div':
        print(float(a)//float(b))
    

oper(firstNum,secondNum)