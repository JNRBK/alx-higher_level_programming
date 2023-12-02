#!/usr/bin/python3
"""function for dividing matrix elements"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
    @matrix = matrix parameter
    @div = parameter for division

    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(r, list) for r in matrix) or
        not all((isinstance(x, int) or isinstance(x, float))
                for x in [y for r in matrix for y in r])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
