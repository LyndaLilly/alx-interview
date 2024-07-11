#!/usr/bin/python3
"""
inside a file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """this calculates fewest no needed from H characters"""
    x = 0
    y = 2
    while n > 1:
        while not n % y:
            x += y
            n /= y
        y += 1
    return x

