#!/usr/bin/python3
""" the lockboxes problem """


def canUnlockAll(boxes):
    """function to solve the lockboxes problem"""
    boxes_visited = set()

    def visit_boxes_recursion(box_index):
        if box_index in boxes_visited:
            return
        boxes_visited.add(box_index)

        keys = boxes[box_index]

        for key in keys:
            visit_boxes_recursion(key)

    visit_boxes_recursion(0)

    return len(boxes_visited) == len(boxes)
