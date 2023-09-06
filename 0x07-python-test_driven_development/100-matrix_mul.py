#!/usr/bin/python3

"""Define a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if type(m_a) != list:
        raise TypeError('m_a must be a list')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    for i in m_a:
        if type(i) != list:
            raise TypeError('m_a must be a list of lists')

        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')

    s_a = set()

    for i in m_a:
        s_a.add(len(i))

    if len(s_a) != 1:
        raise TypeError('each row of m_a must be of the same size')

    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for i in m_b:
        if type(i) != list:
            raise TypeError('m_b must be a list of lists')

        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')

    s_b = set()

    for i in m_b:
        s_b.add(len(i))

    if len(s_b) != 1:
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b[0]) and len(m_a) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        tmp = []
        for j in range(len(m_b)):
            tmp.append(0)

        result.append(tmp)

    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
