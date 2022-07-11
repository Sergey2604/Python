num=int(input('Введите число '))
def krat(a):
     if ((num % 5 == 0 and not num % 30 == 0) and num % 10 == 0) or num % 15 == 0 and (not num % 30 == 0):
         print('da')
     else:
         print('net')
krat(num)
