#!/usr/bin/python3
"""
Contains function canUnlockAll

Alternative Solution
def canUnlockAll(boxes: list) -> bool:
    # check If there are boxes or boxes is not a list
    if not boxes or not isinstance(boxes, list):
        return False
    # Keep a list of opened boxes. The first box is always opened
    openedBoxes = [0]

    def collectKeys(box):
        # Just a routine check
        if not box or not isinstance(box, list):
            return
        # here we loop through the box collect keys and append
        # the associated box to our list of opened boces
        for key in box:
            # since our boxes corrspond to the indexes of our boxes list
            # the keys we need must be less than the length of boxes
            if key < len(boxes) and key not in openedBoxes:
                openedBoxes.append(key)
                collectKeys(boxes[key])
    collectKeys(boxes[0])
    return len(openedBoxes) == len(boxes)
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    visited.add(0)
    queue = [0]

    while queue:
        curr = queue.pop(0)
        for key in boxes[curr]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
