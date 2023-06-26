# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)



class Matrix(object):
    def __init__(self, r,c):
        self.matrix = self.get_matrix(r,c)
    def get_matrix (self,r,c):
        num=1
        matrix=[(None for j in range(c) for i in range (r))]
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                matrix[i][j]=num
                num+=1
        return matrix
    
    def get_matrix_str (self,matrix):
        strings=[]
        for r in matrix:
            strings.append(str(r))
        return '\n'.join(strings)
    
    def __str__(self):
        return self.get_matrix_str(self.matrix)
    def __len__(self):
        return len(self.matrix)
    def add(self.matrix):
        self.content.append(matrix)
    def get_rows_count(self):
        return self.r
    
    def get_columns_count (self):
        return self.c

m=Matrix(4,5)
print (m)


    @property
    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)

        return (rows, cols)


# exec(stdin.read())
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m) == '1\t1\t1\n0\t100\t10')
m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)
