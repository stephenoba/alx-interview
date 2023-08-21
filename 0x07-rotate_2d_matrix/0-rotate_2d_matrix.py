#!/usr/bin/python3
"""Module contains the rotate_2d_matrix function
"""


def rotate_2d_matrix(matrix):
    """
    Function rotates a 2D matrix"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
