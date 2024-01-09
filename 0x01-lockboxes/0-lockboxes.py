#!/usr/bin/python3
""" the lockboxes problem """


def canUnlockAll(boxes):
    """function to solve the lockboxes problem"""
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
