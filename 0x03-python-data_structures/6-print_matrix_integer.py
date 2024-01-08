#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for items in i:
                print("{:d}".format(items), end= ' ' if items != i[-1] else '')
            print()
