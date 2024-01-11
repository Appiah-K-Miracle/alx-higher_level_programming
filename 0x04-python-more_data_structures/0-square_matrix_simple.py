#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_value = matrix.copy()
    for index in range (len(matrix)):
        square_value[index] = list(map(lambda line: line**2, matrix[index]))
    return square_value
