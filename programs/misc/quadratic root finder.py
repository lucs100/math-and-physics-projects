import math
import fractions as frc
from decimal import Decimal
import numbers # neccesary?
# todo - please god add exact value readout, it cant be hard just let the values persist somehow (class?)
# i should relly just redo this, roots are far more important than factoring but it could be done in two modes or just a second file

def quadraticFactor(a, b, c, rootCount):
    global gcd
    gcd = str(math.gcd(int(a), math.gcd(int(b), int(c))))
    if int(gcd) == 1:
        gcd = ''
    if a < 0:
        gcd = '-' + gcd
    result1 = ((Decimal((0)-b) + Decimal(math.sqrt(b ** 2 - (4 * a * c))))/(2 * a))
    result2 = ((Decimal((0)-b) - Decimal(math.sqrt(b ** 2 - (4 * a * c))))/(2 * a))

    pmode = (result1, result2)

    resultPair1 = Decimal.as_integer_ratio(result1)
    resultPair2 = Decimal.as_integer_ratio(result2)

    if resultPair1[1] != 1 or resultPair2[1] != 1:
        return rationalMode(a, b, c, rootCount)

    try:
        result1, result2 = int(result1), int(result2)
    except:
        print("Integer root detection error - debug codes {} and {}.".format(result1, result2))
        exit(1)

    if rootCount == 1:
        if result1 == result2:
            print("Double root found for quadratic {} at x = {}.".format(quadStr, result1))
            print("Factored form: \t {}".format(buildFactoredStr(result1, result1, rootCount)))
            return result1, result1
        else:
            raise Exception("Unexpected float error - {}, {}".format(*pmode))
    elif rootCount == 2:
        print("Roots found for quadratic {} at x = {} and x = {}.".format(quadStr, pmode[0], pmode[1]))
        print("Factored form: \t {}".format(buildFactoredStr(result1, result2, rootCount)))
        return result1, result2

def findDiscriminant(a, b, c):
    d1 = b ** Decimal(2)
    d2 = Decimal(4) * a * c
    if d1 > d2:
        quadraticFactor(a, b, c, 2)
    if d1 == d2:
        quadraticFactor(a, b, c, 1)
    if d1 < d2:
        print("No real roots were found for the quadratic {}.".format(quadStr))
        if singleRun:
            exit(0)

def buildQuadStr(a, b, c):
    if a == b == c == 0:
        print("Quadratic with no value inputted.")
        if singleRun:
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

def buildFactoredStr(a, b, rootCount):
    if a < b:
        a, b = b, a

    a = 0 - a
    b = 0 - b
    
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

    if rootCount == 1:
        return("{}{}{} \t or \t {}²".format(str(gcd), aStr, bStr, aStr))

    return(str(gcd) + aStr + bStr)

def takeInput():
    print("Enter the coefficients of your quadratic: __x² + __x + __, separated by spaces. Variables can be negative. \n")
    a, b, c = [(str(s)) for s in input().split(" ")]
    a, b, c = Decimal(a), Decimal(b), Decimal(c)
    return a, b, c

def quadConfirm(string):
    while True:
        chr = input("Your input quadratic is {}. Is this correct? [Y/N] \n".format(quadStr))
        chr = chr.lower()
        if chr == 'y':
            return True
        elif chr == 'n':
            print("Cancelled.")
            if singleRun:
                exit()
        print("Response must be Y or N.")

def rationalMode(a, b, c, rootCount):
    result1A = frc.Fraction(Decimal((0-b) + Decimal(math.sqrt(b ** 2 - (4 * a * c))))/(2 * a))
    result2A = frc.Fraction(Decimal((0-b) - Decimal(math.sqrt(b ** 2 - (4 * a * c))))/(2 * a))
    result1 = frc.Fraction(Decimal((0-b) + Decimal(math.sqrt(b ** 2 - (4 * a * c))))/(2 * a)).limit_denominator(1000)
    result2 = frc.Fraction(Decimal((0-b) - Decimal(math.sqrt(b ** 2 - (4 * a * c))))/(2 * a)).limit_denominator(1000)
    if result1A != result1 or result2A != result2:
        irrationalMode(result1A, result2A)
        return True
    a1 = result1.numerator
    a2 = result1.denominator 
    b1 = result2.numerator
    b2 = result2.denominator

    if a2 < b2:
        a1, a2, b1, b2 = b1, b2, a1, a2
    a2 = 0 - a2
    b2 = 0 - b2

    if a2 < 0:
        a1, a2 = a1 * Decimal(-1), a2 * Decimal(-1)

    if b2 < 0:
        b1, b2 = b1 * Decimal(-1), b2 * Decimal(-1)

    aStr, bStr = '( ', '( '
    
    if a2 != 1:
        aStr = aStr + str(abs(a2))
    if b2 != 1:
        bStr = bStr + str(abs(b2))
    
    aStr, bStr = aStr + 'x', bStr + 'x'
    
    if a1 < 0:
        aStr = aStr + ' - '
    if b1 < 0:
        bStr = bStr + ' - '
    if a1 > 0:
        aStr = aStr + ' + '
    if b1 > 0:
        bStr = bStr + ' + '

    aStr, bStr = aStr + str(abs(a1)) + ' )', bStr + str(abs(b1)) + ' )'

    finalStr = str(gcd) + aStr + bStr

    if rootCount == 1:
        if result1 == result2:
            print("Double root found for quadratic {} at x = {}.".format(quadStr, result1))
            print("Factored form: \t {}   or    {}²".format(finalStr, aStr))
            return result1, result1
        else:
            raise Exception("Unexpected error - debug codes {}, {}".format(result1, result2))
    elif rootCount == 2:
        print("Roots found for quadratic {} at x = {} and x = {}.".format(quadStr, result1, result2))
        print("Factored form: \t {}".format(finalStr))
        return result1, result2

def irrationalMode(r1, r2):
    r1 = r1.numerator / r1.denominator
    r2 = r2.numerator / r2.denominator
    print("Roots were too imprecise to be calculated as a fraction.")
    if r1 == r2:
        print("Double root found for quadratic {} at x = about {}.".format(quadStr, r1))
        return r1, r2
    else:
        print("Roots found for quadratic {} at x = about {} and x = about {}.".format(quadStr, r1, r2))
        return r1, r2

def runProcess(mode=True): 
    global inputSet
    global quadStr
    global singleRun
    singleRun = mode
    inputSet = takeInput()
    quadStr = buildQuadStr(*inputSet)
    if singleRun:
        quadConfirm(quadStr)
    findDiscriminant(*inputSet)
    print()

runProcess(False)
