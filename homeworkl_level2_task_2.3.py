# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

#def switch_it_up(number):
    

a=int(input ('введи цифру='))

if a>9 and a<0:
    print ('введите цифрц от 0 до 9')
dat={ 0:'zero',
     1: 'one',
     2: 'two',
     3: 'three',
     4: 'four',
     5: 'five',
     6: 'six',
     7: 'seven',
     8: 'eith',
     9: 'nine'
          }
def switch_it_up(a):
    for i in dat:
        b=dat.get(a)
        print ('->',b)
switch_it_up(a)



