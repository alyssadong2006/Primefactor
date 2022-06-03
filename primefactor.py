def generate_prime_factors(number):
    pFactors=[]

    if not isinstance(number,int):
        raise ValueError("Please type number.")

    for i in range(2,number+1):
        if number % i == 0:
            count = 1
            for j in range(2,(i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                pFactors.append(i)
    return pFactors
