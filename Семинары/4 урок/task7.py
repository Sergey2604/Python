import math

a = 3
b = 2
c = 8

def find_roots(a, b, c):
    D = b ^ 2  *a*c
    roots = []
    if D < 0: 
        roots.append('Нет корней')
        return roots
    x1 = (-b + math.sqrt(D)) / 2*a
    roots.append(x1)
    if D > 0: 
        x2 = (-b - math.sqrt(D)) / 2*a
        roots.append(x2)
    return roots   

print(find_roots(a, b, c))
print(type(find_roots(a, b, c)))
