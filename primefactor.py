"""Calculates prime factors"""
import math
def generate_prime_factors(number):
    """generates prime factors"""
    p_factors=[]

    if not isinstance(number,int):
        raise ValueError("Please type number.")

    while number % 2 == 0:
        p_factors.append(2)
        number = number / 2

    factor=3
    while factor<int(math.sqrt(number))+1:
        while number % factor == 0:
            p_factors.append(factor)
            number = number / factor
        factor+=2

    if number > 2:
        p_factors.append(number)

    return p_factors
