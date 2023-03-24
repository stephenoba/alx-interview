#!/usr/bin/env python3
# 0-pascal_triangle

def pascal_triangle(n: int) -> list:
    """
    returns a list of lists representing the Pascal Triangle
    """
    if not isinstance(n, int) or n <= 0:
        return []
    
    # initiate the first step  of triangle
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        # since all rows in a pascal triangle starts with one
        # the new list is initiated with a value of 1
        new = [1]
        for j in range(1, len(prev)):
            new.append(prev[j - 1] + prev[j])
        new.append(1)
        triangle.append(new)

    return  triangle

print(pascal_triangle(5))