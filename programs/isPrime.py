from math import ceil, sqrt
#returns 1 as composite

def isPrime(x):
    if x > 6 and (x % 6 == 1 or x % 6 == 5):
        limit = ceil(sqrt(x))
        for i in range(2, (limit+1)):
            if x % i == 0:
                return False
        return True
    return (x == 2 or x == 3 or x == 5)