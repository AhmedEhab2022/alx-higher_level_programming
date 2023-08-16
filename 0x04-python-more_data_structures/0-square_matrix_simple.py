#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        square_matrix = []
        for i in matrix:
            list_sq = []
            for j in i:
                list_sq.append(j * j)
            square_matrix.append(list_sq)
        return square_matrix
