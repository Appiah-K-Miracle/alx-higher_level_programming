#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for index in matrix:
            for items in index:
                print("{:d}".format(items), end= ' ' if items != index[-1] else ' ')
            print()
