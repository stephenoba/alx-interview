#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    # Initialize perimeter to 0
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land
            if grid[r][c] == 1:
                # Check the four neighbors
                # Check above
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1

                # Check below
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1

                # Check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1

                # Check right
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1
    return perimeter
