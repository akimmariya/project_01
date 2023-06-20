# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

import sqlite3

connection =sqlite3.connect ('teachers.db')
cursor = connection.cursor()
query='''INSERT INTO Students (Student_Id, Student_Name, School_Id) 
VALUES 
('201', 'Иван', '1'), 
('202', 'Петр', '2'), 
('203', 'Анастасия', '3'), 
('204', 'Игорь', '4');
'''
cursor.execute(query)
connection.commit()
connection.close()