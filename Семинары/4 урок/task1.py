""" 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    
    *Пример:*
    
    - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

def OddPositionSum(my_list):
    sum=0
    for i in range(0,len(my_list)):
        if (i%2)>0:
            sum=sum+float(my_list[i])
        else:
            continue
    return sum

my_str=input("Enter your list. Use the whitespace to separate elements.: ")
my_list=my_str.split()
result=OddPositionSum(my_list)
print(f"Sum of all elements on odd positions is {result}")
