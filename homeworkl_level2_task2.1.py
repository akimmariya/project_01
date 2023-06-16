# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

from random import randint
n=10

date=[]
for i in range(n):
    date.append(randint(1,99))

def minimum(date):
    for i in range (len(date)-1):
        for j in range (len(date)-1):
            if date[j]>date[j+1]:
                date[j],date[j+1]=date[j+1], date[j]
    print (date, '-> min=',date[0])
    return date
minimum (date)

def maximum(date):
    for i in range (len(date)-1):
        for j in range (len(date)-1):
            if date[j]>date[j+1]:
                date[j],date[j+1]=date[j+1], date[j]
    print (date, '-> max=',date[9])
    return date
maximum (date)