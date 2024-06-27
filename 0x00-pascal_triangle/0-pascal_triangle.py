#!/usr/bin/python3
"""
this is pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    xy = []
    if n <= 0:
        return xy
    xy = [[1]]
    for i in range(1, n):
        temp = [1]
        for ab in range(len(xy[i - 1]) - 1):
            curr = xy[i - 1]
            temp.append(xy[i - 1][ab] + xy[i - 1][ab + 1])
        temp.append(1)
        xy.append(temp)
    return xy
