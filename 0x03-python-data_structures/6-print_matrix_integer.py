#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        rows = ""
        for element in row:
            rows += "{:d} ".format(element)
        print(rows.rstrip())
