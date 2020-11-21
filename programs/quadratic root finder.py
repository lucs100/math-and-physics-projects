import math
import string

def quadraticFactor(a, b, c, rootCount):
    result1 = (((0-b) + math.sqrt(b ** 2 - (4 * a * c))) / 2 * a)
    result2 = (((0-b) - math.sqrt(b ** 2 - (4 * a * c))) / 2 * a)
    pmode = (result1, result2)
    if rootCount == 1:
        if result1 == result2:
            print("Double root found for quadratic {} at x = {}.".format(quadStr, result1)) 
            return result1
        else:
            raise Exception("Float error - {}, {}".format(*pmode))
    elif rootCount == 2:
        print("Roots found for quadratic {} at x = {} and x = {}.".format(quadStr, (*pmode)))
    return result1, result2

def findDiscriminant(a, b, c):
    d1 = b ^ 2
    d2 = 4 * a * c
    if d1 > d2:
        quadraticFactor(a, b, c, 2)
    if d1 == d2:
        quadraticFactor(a, b, c, 1)
    if d1 < d2:
        print("No real roots were found for the quadratic {}.".format(quadStr))

def buildStr(a, b, c):
    if a == b == c == 0:
        print("Quadratic with no value inputted.")
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
        out = out + str(abs(c)) + ' '
    
    # these three processes aren't viable to loop through, because too much differs between each iteration
            
    return out

def takeInput():
    print("Enter the coefficients of your quadratic - ()x² + ()x + (), separated by spaces. Variables can be negative. \n")
    return list(map(int, input().split()))

def quadConfirm(string):
    while True:
        chr = input("Your input string is {}. Is this okay? [Y/N] \n".format(quadStr))
        chr = chr.lower()
        if chr == 'y':
            return True
        elif chr == 'n':
            print("Cancelled.")
            exit()
        print("Response must be Y or N.")

def runProcess(): 
    global inputSet
    global quadStr
    inputSet = takeInput()
    quadStr = buildStr(*inputSet)
    quadConfirm(quadStr)
    findDiscriminant(*inputSet)

runProcess()