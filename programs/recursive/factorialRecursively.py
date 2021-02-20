cache = dict()

cache[0] = 1
cache[1] = 1
cache[2] = 2

def factorial(n):
    if n in cache:
        return cache[n]
    cache[n] = n*factorial(n-1)
    return cache[n]

for i in range(10):
    print(factorial(int(input())))

print(cache)

# CAUTION - THESE PROGRAMS CAN BE EXTREMELY RESOURCE INTENSIVE AND HANG YOUR COMPUTER. USE AT YOUR OWN RISK