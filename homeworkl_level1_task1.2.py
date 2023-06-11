# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],] 

import random
x= (random.choice(my_favorite_songs)[1]) + random.choice(my_favorite_songs)[1] +random.choice(my_favorite_songs)[1]
x=round (x)
print ('Три песни звучат', x , 'минут ' )

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
import random
z=random.choice(list(my_favorite_songs_dict))
n=random.choice(list(my_favorite_songs_dict))
m=random.choice(list(my_favorite_songs_dict))
l=(my_favorite_songs_dict[z])+(my_favorite_songs_dict[n])+(my_favorite_songs_dict[m])
print ('Три песни звучат',round(l), ' минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random
print ('случайная песня пункта А:', random.choice(my_favorite_songs))
print ('случайная песня пункта b:', random.choice(list (my_favorite_songs_dict)))



# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
my_favorite_songs = [
    ['Waste a Moment',  (3.03)],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],] 

import datetime
x= datetime.time (my_favorite_songs[1])
print (x)
