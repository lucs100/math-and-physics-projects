import math

# todo:
# get extra functions (commented out) working
# pass list of lists into addVectors() rather than two lists then iterate over all components to build list of all x/y comps
#   wouldnt be too hard because component evaluation already uses lists

def addVectors(vectorSet):
    xComponents, yComponents = [], []
    for i in range(len(vectorSet)):
        xComponents.append(vectorSet[i][0] * math.cos(math.radians(vectorSet[i][1])))
        yComponents.append(vectorSet[i][0] * math.sin(math.radians(vectorSet[i][1])))
    # if unitsAreEqual == False:
    #     magB = (magB * unitFactor)
    # xComponents.append(magB * (math.cos(math.radians(dirB))))
    # yComponents.append(magB * (math.sin(math.radians(dirB))))
    xMag, yMag = sum(xComponents), sum(yComponents)
    if xMag == 0:
        if yMag > 0:
            finalDir = 90
        elif yMag < 0:
            finalDir = 270
        else:
            print("Resultant vector was zero.")
            return 0
    if yMag == 0:
        if xMag > 0:
            finalDir = 0
        elif xMag < 0:
            finalDir = 180
        else:
            print("Resultant vector was zero.")
            return 0
    else:
        finalDir = math.atan(yMag/xMag)
    # if degreesMode:
    #     finalDir = math.degrees(finalDir)
    finalMag = (math.sqrt((xMag ** 2) + (yMag ** 2)))
    finalDir = math.degrees(finalDir)
    if finalDir < 0:
        finalDir = finalDir + 360
    if 0 < finalDir and finalDir < 90:
        #first quad
        pass
    elif 90 < finalDir and finalDir < 180:
        #second quad
        pass
    elif 180 < finalDir and finalDir < 270:
        #third quad
        pass
    elif 270 < finalDir and finalDir < 360:
        #fourth quad
        pass
    vector = finalMag, finalDir
    printTuple = (round(finalMag, sigs), unitName, round(finalDir, sigs))
    if degreesMode:
        print("Resultant vector has a magnitude of {}{} and a direction of {}° in standard position.".format(*printTuple))
    # elif degreesMode == False:
    #     print("Final vector has a magnitude of {}{} and a direction of {}rad in standard position.".format(*printTuple))
    return vector

def inputToVector(name):
    magnitude = ''
    while magnitude == '':
        magnitude = input("Input {}'s magnitude:  ".format(name))
    magnitude = float(magnitude)
    direction = ''
    if degreesMode == True:
        while direction == '':
            direction = input("Input {}'s direction in degrees, when in terminal position ([E] = 0°):  ".format(name))
        direction = float(direction)
        vector = (magnitude, direction)
        print("Created vector \"{}\" with magnitude {}{} and direction {}°.".format(name, vector[0], unitName, vector[1]))
    # elif degreesMode == False:
    #     while direction == '':
    #         dirStr = str(input("Input {}'s direction in radians, when in terminal position ([E] = 0rad, use (math.pi) to represent π):  ".format(name)))
    #     direction = math.radians(float(compile(dirStr, '<string>', "single")))
    #     vector = (magnitude, direction)
    #     print("Created vector \"{}\" with magnitude {}{} and direction {}rad.".format(name, vector[0], unitName, round(vector[1], 3)))
    #todo - show proper unit for angle
    return vector

def askUserQuestion(question, responseT, responseF):
    while True:
        print("{} {}/{}   ".format(question, responseT.upper(), responseF.upper()), end="")
        response = input()
        response = response.lower()
        if response == responseT:
            return True
        elif response == responseF:
            return False
        else:
            print("Input invalid - please respond with \"{}\" or \"{}\".".format(responseT.upper(), responseF.upper()))

def unitConversionMode():
    print("Your second unit will be converted to your first unit. \n Enter a factor to multiply your second unit by.")
    global unitFactor 
    unitFactor = float(input())
    print("Factor of {} set.")
    pass

def askUnit():
    if unitsAreEqual:   
        print("Enter the name or symbol of your magnitude unit. Press enter to ignore units.")
    else:
        print("Enter the name or symbol of your first vector's magnitude unit.")
    return str('' + str(input()))

def askSigs():
    outputToParse = (input("Enter number of significant decimal places. Press enter to default to one.   "))
    if outputToParse == '' or bool(outputToParse.isnumeric()) == False:
        return 1
    return int(outputToParse)

def askVectorCount():
    outputToParse = (input("Enter number of vectors. Press enter to default to two.   "))
    if outputToParse == '' or bool(outputToParse.isnumeric()) == False:
        return 2
    return int(outputToParse)

def runProcess():
    global unitsAreEqual
    global degreesMode
    global unitName
    global sigs
    global vector1
    global vector2
    # unitsAreEqual = askUserQuestion("Are your units of magnitude equal?", 'y', 'n')
    unitsAreEqual = True
    # degreesMode = askUserQuestion("Are your units of angle in degrees or radians?", 'd', 'r')
    degreesMode = True
    unitName = askUnit()
    # unitName = " units" # space is neccesary for spacing of output prints
    sigs = askSigs()
    vectorCount = askVectorCount()
    listOfVectors = []
    for i in range(vectorCount):
        listOfVectors.append(inputToVector("vector{}".format(i+1)))
    print(listOfVectors)
    addVectors(listOfVectors)

runProcess()