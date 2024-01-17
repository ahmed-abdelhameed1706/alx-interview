#!/usr/bin/env python3
"""function to find the mininmum operation"""
import math


def gcd(n):
    result = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result = max(result, i, n // i)
    return result


def is_prime(number):
    """function to find if number is prime"""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def minOperations(n: int) -> int:
    """function to find minimum operations"""
    if n <= 0:
        return 0

    if is_prime(n) or n == 1:
        return n

    gcd_n = gcd(n)
    div_factor = n // gcd_n

    if is_prime(gcd_n) or gcd_n == 1:
        return gcd_n + div_factor
    return minOperations(gcd_n) + div_factor
