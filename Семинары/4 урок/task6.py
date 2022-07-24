n = '1 23 32 536 66 604 12'
list = n.split(' ')

list = [int(s) for s in n.split()]

print(list)
max = max(list)
min = min(list)

print(list)
print(f'max - {max} min - {min}')
print(type(list[0]))
