#!/usr/bin/python3
"""
this solves the lockboxes issues
"""


def canUnlockAll(boxes):
    """
    this shows if a series of locked boxes can be opened
    according to keys that can be gotten.
    this solves the lockboxes issues
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for m in range(1, len(boxes) - 1):
        boxcheck = False
        for nb in range(len(boxes)):
            boxcheck = m in boxes[nb] and m != nb
            if boxcheck:
                break
        if boxcheck is False:
            return boxcheck
    return True
