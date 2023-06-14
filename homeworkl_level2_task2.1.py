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



a,b,c=input('a'), input ('b'), input ('c')
d=[a,b,c]
def minimum():
    for i in d:
        if a<b and a<c:
            print ('минимум=', a)
        if b<a and b<c:
            print ('минимум=', b)
        if c<a and c<b:
            print ('минимум=', c)
    return minimum      
minimum()

def maximum():
    for i in d:
        if a>b and a>c:
            print ('максимум=', a)
        if b>a and b>c:
            print ('максимум=', b)
        if c>a and c>b:
            print ('максимум=', c)
    return maximum     
maximum()
#def maximum(arr)
# pass