#!/usr/bin/python3
"""
Module contains the function makeChange(coins, total)
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    a give total amount.
    """
    if total == 0:
        return 0
    # Initialize the dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the dp array
    for c in coins:
        for i in range(c, total + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    # Check if the total can be reached
    return -1 if dp[total] == float('inf') else dp[total]
