# port of a lua hash function I wrote called quickHash.
# please don't use this for sensitive information.
# no seriously please, it's incredibly unsafe

import random
import math

number = int(input())

def quickHash(input):
    random.seed(input)
    input += 100
    oper1 = random.randrange(1000, 1000000)
    oper2 = random.randrange(1000, 1000000)
    flow = random.randrange(1, 4)
    output = 0
    if flow == 1:
        output = (input * oper1 * oper2)
    elif flow == 2:
        output = ((((input**2) * oper1) / math.sqrt(oper2)) * oper2)
    elif flow == 3:
        output = (((input**3) / abs(oper1 - oper2))**2)
    elif flow == 4:
        output = (math.sqrt((input % 10) * (oper1**2) * (oper2**2)))
    while output < 1000000:
        output = ((output * oper1 * oper2) + 1)
    return (math.ceil(output % 1000000))

print("Encoded as {}.".format(quickHash(number)))

