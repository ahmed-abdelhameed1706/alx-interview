#!/usr/bin/python3
""" the lockboxes problem """


def canUnlockAll(boxes):
    """function to solve the lockboxes problem"""
    boxes_visited = set()

    def visit_boxes_recursion(box_index):
        if box_index in boxes_visited:
            return False

        boxes_visited.add(box_index)

        keys = boxes[box_index]

        flag = False

        for key in keys:
            if visit_boxes_recursion(key):
                flag = True

        return flag

    visit_boxes_recursion(0)

    return len(boxes_visited) == len(boxes)
