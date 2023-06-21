# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def get_connection():
    connection =sqlite3.connect ('teachers.db')
    return connection
def close_connection(connection):
    if connection:
        connection.close()


def get_student_id(student_id):
    try:
        connection = get_connection()
        cursor= connection.cursor()
        quary='''SELECT * from School
        JOIN Students on School.school_id=Students.school_id where student_id=?
       '''
        cursor.execute(quary, (student_id,))
        records= cursor.fetchall()
        for row in records:
            print ("Student_Id", row[0], )
            print ("Student_Name", row[4], )
            print ("School_id", row[3], )
            print ("School_name", row[1], )
                             
        close_connection(connection)
       
    except (Exception, sqlite3.Error) as error:
        print ('ошибка получения данных', error)

get_student_id(202)