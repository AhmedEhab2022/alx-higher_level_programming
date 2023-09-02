#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Takes a matrix and number and divide
    all numbers in the matrix by the given number and
    store the result in a new matrix and return it.

    Args:
        matrix: the given matrix to divide values in it.
        div: the number that the matrix divided by.

    Return:
        a new matrix with results of divides all values in matrix matrix
        by number div, if cannot do the operation the function
        raise the suitable error.
    """

    te1_matrix = 'matrix must be a matrix (list of lists) of integers/floats'
    te2_matrix = 'Each row of the matrix must have the same size'
    te_div = 'div must be a number'
    zde_div = 'division by zero'

    s = set({})
    if type(matrix) != list:
        raise TypeError(te1_matrix)

    for i in matrix:
        if type(i) != list:
            raise TypeError(te1_matrix)

        s.add(len(i))
        for j in i:
            if type(j) not in [float, int]:
                raise TypeError(te1_matrix)

    if len(s) > 1:
        raise TypeError(te2_matrix)

    if type(div) not in [int, float]:
        raise TypeError(te_div)

    if div == 0:
        raise ZeroDivisionError(zde_div)

    new_matrix = []
    for i in matrix:
        tmp = []
        for j in i:
            tmp.append(round(j / div, 2))

        new_matrix.append(tmp)

    return new_matrix
