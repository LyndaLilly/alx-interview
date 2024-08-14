#!/usr/bin/python3

""" this rotates the 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ this is a method for rotating 2D Matrix 90 degrees clockwise
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
    """

    n = len(matrix[0])

    for x in range(n - 1, -1, -1):
        for y in range(0, n):
            matrix[y].append(matrix[x].pop(0))
