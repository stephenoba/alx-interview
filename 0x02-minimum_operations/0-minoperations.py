#!/usr/bin/python3
"""
Module contains solution to min operations question
"""


def minOperations(n):
    """
    method that calculates the fewest number of
    operations needed to result in exactly `n` `H`
    characters in the file.

    Args
    ----
    n(int): Number of times to call the operations

    Returns
    -------
    An integer
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
