#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """this gets the operations needed to result in n H characters"""
    xy = 0
    yx = 2
    while n > 1:
        while not n % yx:
            xy += yx
            n /= yx
        yx += 1
    return xy
