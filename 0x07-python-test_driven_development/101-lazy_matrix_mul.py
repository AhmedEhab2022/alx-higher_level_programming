#!/usr/bin/python3

import numpy as np

"""Define a function that multiplies 2 matrices by using the module NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy"""

    return (np.matmul(m_a, m_b))
