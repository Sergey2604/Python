list = [int(i) for i in input().split()]
max = list[0]
def sravnenie(list):
    for i in range (1, len(list)):
        if max < list[i]:
            max = list[i]
print(max)
sravnenie(list)