#!/usr/bin/python3
"""making change function"""


def makeChange(coins, total):
    """function to know the lowest number of coins"""
    if total <= 0:
        return 0

    memo = [float("inf")] * (total + 1)
    memo[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            memo[i] = min(memo[i - coin] + 1, memo[i])

    return memo[total] if memo[total] != float("inf") else -1
