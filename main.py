# 📌Создайте класс Матрица.
# Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:

    def __init__(self, matrix):
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Размер матриц должен совпадать!')
        result_matrix = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result_matrix)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('Количество столбцов в первой матрице должно быть равно количеству строк в другой!')
        result_matrix = [[0 for i in range(len(self.matrix))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                for k in range(len(self.matrix[0])):
                    result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result_matrix)


a = Matrix([[2, 4], [3, 1], [5, 6]])
b = Matrix([[4, 4, 2], [3, 1, 6]])
c = Matrix([[3, 1, 2], [0, 5, 2]])
print(a*b)
print(c+b)