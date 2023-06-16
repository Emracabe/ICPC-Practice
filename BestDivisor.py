"""
    Link: https://www.hackerrank.com/challenges/best-divisor/problem?h_r=profile
    Description:
        Kristen loves playing with and comparing numbers. 
        She thinks that if she takes two different positive numbers, 
        the one whose digits sum to a larger number is better than the other.
        If the sum of digits is equal for both numbers, then she thinks the smaller number is better.
        For example, Kristen thinks that 13  is better than  31 and that  12 is better than 11.

        Given an integer, n, can you find the divisor of  n that Kristin will consider to be the best?
"""

import math
import os
import random
import re
import sys

def digit_sum(number):
    return sum(int(digit) for digit in str(number))

def best_divisor(n):
    best_divisor = n
    best_sum = digit_sum(n)

    for divisor in range(1, n):
        if n % divisor == 0:
            divisor_sum = digit_sum(divisor)
            
            if divisor_sum > best_sum:
                best_divisor = divisor
                best_sum = divisor_sum
            elif divisor_sum == best_sum and divisor < best_divisor:
                best_divisor = divisor

    return best_divisor

if __name__ == '__main__':
    n = int(input().strip())

    print(best_divisor(n))