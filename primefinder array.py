import math

for i in range(40):
    print()

#startEnumerate = int(input("Enter a start range:"))
startEnumerate = 6
print("Program begins searching at 6.")
maxEnumerate = int(input("Enter a stop range:"))

currentNumber = startEnumerate

primeTable = [2, 3, 5]

print("Primes from", startEnumerate, "to", maxEnumerate, ":")

while currentNumber < maxEnumerate:
    currentNumber += 1
    divisorIndex = 1
    divisorToTest = primeTable[divisorIndex]
    if (currentNumber % 6 == (1 or 5)):
        while divisorToTest < (math.sqrt(currentNumber)):
            if currentNumber % divisorToTest == 0:
                #not prime
                break
            else:
                divisorIndex += 1
        #is prime
        primeTable.append(currentNumber)
        print(currentNumber, end=", ")
print("no primes remaining.")
        