import math

for i in range(40):
    print()

startEnumerate = int(input("Enter a start range:"))
maxEnumerate = int(input("Enter a stop range:"))

currentNumber = startEnumerate

print("Primes from", startEnumerate, "to", maxEnumerate, ":")

while currentNumber < maxEnumerate:
    currentNumber += 1
    divisorToTest = 2
    if (currentNumber % 6 == (1 or 5)):
        while divisorToTest < (math.sqrt(currentNumber)):
            if currentNumber % divisorToTest == 0:
                #not prime
                break
            else:
                divisorToTest += 1
        print(currentNumber, end=", ")
print("no primes remaining.")
    
    
        