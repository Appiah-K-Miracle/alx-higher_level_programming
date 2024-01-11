#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_value = [ ]
    for index in matrix:
        square_value.append([num**2 for num in index])
    return square_value
