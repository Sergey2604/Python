def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input('Введите число элементов: '))

def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibo(i))
    return list
print(fibolist(x))
