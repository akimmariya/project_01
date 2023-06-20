# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3
connection=sqlite3.connect('teachers.db')
cursor=connection.cursor()
query= '''JOIN School ON School.School_id=Students.School_id'''
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3

