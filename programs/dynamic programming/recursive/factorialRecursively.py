cache = dict()

cache[0] = 1
cache[1] = 1
cache[2] = 2

def factorial(n):
    if n in cache:
        return cache[n]
    cache[n] = n*factorial(n-1)
    return cache[n]

while True:
    x = int(input())
    while (x - (max(cache.keys()))) > 950:
        y = max(cache.keys()) + 950
        factorial(y)
    print(factorial(x))

# CAUTION - THESE PROGRAMS CAN BE EXTREMELY RESOURCE INTENSIVE AND HANG YOUR COMPUTER. USE AT YOUR OWN RISK