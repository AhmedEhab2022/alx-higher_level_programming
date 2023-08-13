#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix[0])
    for i in matrix:
        cnt = 0
        for j in i:
            if cnt + 1 < row:
                print("{:d}".format(j), end=' ')
            else:
                print("{:d}".format(j), end='')
            cnt += 1
        print()
