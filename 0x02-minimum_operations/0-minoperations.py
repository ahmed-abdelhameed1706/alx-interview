#!/usr/bin/python3
"""function to find the mininmum operation"""
import math


def minOperations(n: int) -> int:
    """function to find minimum operations"""

    def gcd(n: int) -> int:
        """function to find the greatest number to divide n by"""
        result = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                result = max(result, i, n // i)
        return result

    def is_prime(number: int) -> bool:
        """function to find if number is prime"""
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def rec_min(x: int) -> int:
        """function to recursivly find the operations"""
        if x <= 0:
            return 0

        if is_prime(x) or n == 1:
            return x

        gcd_n = gcd(x)
        div_factor = x // gcd_n

        if is_prime(gcd_n) or gcd_n == 1:
            return gcd_n + div_factor
        return minOperations(gcd_n) + div_factor

    return rec_min(n)
