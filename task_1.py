class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = '\n'.join([' '.join(map(str, line)) for line in self.matrix])
        return res

    def __add__(self, other):
        res = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
               for i in range(len(self.matrix))]
        return res


my_matrix = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
my_matrix2 = Matrix([[3, 2, 1], [6, 5, 4], [7, 6, 5]])
print(Matrix(my_matrix + my_matrix2))
