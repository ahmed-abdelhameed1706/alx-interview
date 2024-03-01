#!/usr/bin/python3
"""making change function"""


def makeChange(coins, total):
    """function to know the lowest number of coins"""

    if total <= 0:
        return 0

    count = 0

    coins.sort(reverse=True)

    for coin in coins:
        if total <= 0:
            break

        count = count + (total // coin)
        total = total % coin

    if total == 0:
        return count
    else:
        return -1
