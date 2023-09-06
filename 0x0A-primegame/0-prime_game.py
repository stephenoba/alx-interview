#!/usr/bin/python3
"""Module contains the isWinner function
"""


def isWinner(x, nums):
    """
    Funtion implements algorithm to get winner.
    """
    # Implement Sieve of Eratosthenes to get prime numbers up to max(nums)
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1

    # Count number of prime numbers up to n for each n in nums
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i-1] + int(is_prime[i])

    # Simulate the game and count the number of rounds each player wins
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        # Maria wins if there is an odd number of primes up to n
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
