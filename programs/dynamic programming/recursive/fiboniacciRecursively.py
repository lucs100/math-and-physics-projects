cache = dict()

cache[0] = 0
cache[1] = 1
cache[2] = 1

def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = (fib(n-1) + fib(n-2))
    return cache[n]

while True:
    x = int(input())
    while (x - (max(cache.keys()))) > 950:
        y = max(cache.keys()) + 950
        fib(y)
    print(fib(x))

# CAUTION - THESE PROGRAMS CAN BE EXTREMELY RESOURCE INTENSIVE AND HANG YOUR COMPUTER. USE AT YOUR OWN RISK