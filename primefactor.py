import math
def generate_prime_factors(n):
    pFactors=[]

    if not isinstance(n,int):
        raise ValueError("Please type number.")

    while n % 2 == 0:
        pFactors.append(2)
        n = n / 2

    factor=3
    while factor<int(math.sqrt(n))+1:
        while (n % i == 0):
            pFactors.append(i)
            n = n / i
        factor+=2

    if n > 2:
        pFactors.append(n)

    return pFactors
