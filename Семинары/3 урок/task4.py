import json
list=[]
n = int(input('Введите число n -> '))
def list_def(n):
    for i in range(-n, n+1):
        list.append(i)
    return list
list_def(n)
print(list)
with open('data1.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
    
            fh.write(json.dumps(list, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
print('БД успещно сохранена')