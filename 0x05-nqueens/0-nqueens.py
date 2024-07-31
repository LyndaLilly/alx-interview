#!/usr/bin/python3
""" this is the queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

num = int(sys.argv[1])


def queens(num, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < num:
        for j in range(num):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(num, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(num):
    """ solve """
    k = []
    i = 0
    for solution in queens(num, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(num)
