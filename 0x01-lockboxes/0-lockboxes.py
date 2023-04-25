#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = [key for key in boxes[0]]
    while queue:
        key = queue.pop(0)
        if key < n and not opened[key]:
            opened[key] = True
            queue.extend(boxes[key])
    return all(opened)
