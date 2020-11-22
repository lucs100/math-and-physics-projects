import math, string
from fractions import Fraction

def quadraticFactor(a, b, c, rootCount):
    result1 = (((0-b) + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
    result2 = (((0-b) - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
    pmode = (round(result1, 3), round(result2, 3))

    resultPair1 = float.as_integer_ratio(result1)
    resultPair2 = float.as_integer_ratio(result2)

    if resultPair1[1] != 1 or resultPair2[1] != 1:
        resultPair1[0], resultPair1[1], resultPair2[0], resultPair2[1] == Fraction(resultPair1[0]), Fraction(resultPair1[1]), Fraction(resultPair2[0]), Fraction(resultPair2[1])
        return rationalMode(result1, *resultPair1, result2, *resultPair2, rootCount)

    if rootCount == 1:
        if result1 == result2:
            print("Double root found for quadratic {} at x = {}.".format(quadStr, result1))
            print("Factored form: \t {}".format(buildFactoredStr(result1, result1)))
            return result1
        else:
            raise Exception("Unexpected float error - {}, {}".format(*pmode))
    elif rootCount == 2:
        print("Roots found for quadratic {} at x = {} and x = {}.".format(quadStr, (*pmode)))
        print("Factored form: \t {}".format(buildFactoredStr(result1, result2)))
        return result1, result2

def findDiscriminant(a, b, c):
    d1 = b ** 2
    d2 = 4 * a * c
    if d1 > d2:
        quadraticFactor(a, b, c, 2)
    if d1 == d2:
        quadraticFactor(a, b, c, 1)
    if d1 < d2:
        print("No real roots were found for the quadratic {}.".format(quadStr))
        if singleMode:
            exit()

def buildQuadStr(a, b, c):
    if a == b == c == 0:
        print("Quadratic with no value inputted.")
        if singleMode:
            exit(000)

    # no need for sign of A because it precedes the coefficient without a space
    out = ''
    if a != 0:
        if abs(a) != 1:
            out = out + str(a)
        out = out + 'x² '

    if b != 0:
        if b < 0:
            out = out + '- ' 
        if b > 0:
            out = out + '+ '
        if abs(b) == 1:
            out = out + 'x '
        else:
            out = out + str(abs(b)) + 'x '

    if c != 0:
        if c < 0:
            out = out + '- ' 
        if c > 0:
            out = out + '+ '
        out = out + str(abs(c))
    
    # these three processes aren't viable to loop through, because too much differs between each iteration
            
    return out

def buildFactoredStr(a, b):
    if a < b:
        a, b = b, a
    a = 0 - a
    b = 0 - b
    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)
    aStr, bStr = "(x", "(x"
    if a < 0:
        aStr = aStr + ' - '
    if a > 0:
        aStr = aStr + ' + '
    if a == 0:
        aStr = aStr + ')'
    else:
        aStr = aStr + str(abs(a)) + ')'

    if b < 0:
        bStr = bStr + ' - '
    if b > 0:
        bStr = bStr + ' + '
    if b == 0:
        bStr = bStr + ')'
    else:
        bStr = bStr + str(abs(b)) + ')'

    return(aStr + bStr)

def takeInput():
    print("Enter the coefficients of your quadratic: __x² + __x + __, separated by spaces. Variables can be negative. \n")
    return list(map(float, input().split()))

def quadConfirm(string):
    while True:
        chr = input("Your input quadratic is {}. Is this okay? [Y/N] \n".format(quadStr))
        chr = chr.lower()
        if chr == 'y':
            return True
        elif chr == 'n':
            print("Cancelled.")
            if singleMode:
                exit()
        print("Response must be Y or N.")

def runProcess(single=True): 
    global singleMode
    singleMode = single
    global inputSet
    global quadStr
    inputSet = takeInput()
    quadStr = buildQuadStr(*inputSet)
    if singleMode:
        quadConfirm(quadStr)
    findDiscriminant(*inputSet)

def rationalMode(a, a1, a2, b, b1, b2, rootCount):
    # a = result1
    # a1 = result1's numerator
    # a2 = result1's denominator 
    # b = result2
    # b1 = result2's numerator
    # b2 = result2's denominator
    # rootCount = 1 or 2

    if a2 < b2:
        a2, b2 = b2, a2
    a2 = 0 - a2
    b2 = 0 - b2

    if a1 < 0 and a2 < 0:
        a1, a2 = abs(a1), abs(a2)

    if b1 < 0 and b2 < 0:
        b1, b2 = abs(b1), abs(b2)

    aStr, bStr = '(' + '('

    if a2 < 0:
        aStr = aStr + '-'
    if b2 < 0:
        bStr = bStr + '-'
    
    if a2 != 1:
        aStr = aStr + str(abs(a2)) + 'x'
    if b2 != 1:
        bStr = bStr + str(abs(b2)) + 'x'
    
    if a1 < 0:
        aStr = aStr + '-'
    if b1 < 0:
        bStr = bStr + '-'
    if a1 > 0:
        aStr = aStr + ' + '
    if b1 > 0:
        bStr = bStr + ' + '

    aStr, bStr = aStr + str(abs(a1)) + ')', bStr + str(abs(b1)) + ')'

    finalStr = aStr + bStr

    print("Entered rational mode!")
    if rootCount == 1:
        if a == b:
            print("Double root found for quadratic {} at x = {}.".format(quadStr, a))
            print("Factored form: \t {}".format(finalStr))
            return a
        else:
            raise Exception("Unexpected float error - {}, {}".format(a, b))
    elif rootCount == 2:
        print("Roots found for quadratic {} at x = {} and x = {}.".format(quadStr, a, b))
        print("Factored form: \t {}".format(finalStr))
        return a, b

while True:
    print("\n\n")
    runProcess(False)