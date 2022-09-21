from random import randint, choice
import time
from tracemalloc import start

# Prototype for MTE 201 Lab 1
# Lucas Di Pietro, 2022

# no seed uses current system time as seed

KnownAreaCodes = ["519", "905", "289", "365"]

trials = 0
trialsValid = 0

class Number:
    def __init__(self):
        ac0 = choice(KnownAreaCodes)
        finalNum = int(ac0)
        finalStr = str(ac0) + '-'
        for i in range(1+3, 11):
            n = randint(0, 9)
            finalNum += int(n)
            finalStr += str(n)
            if i == 6:
                finalStr += '-'
        self.ac = ac0
        self.num = finalNum
        self.string = finalStr

    def __repr__(self):
        return self.string

class Response:
    def __init__(self, correct0, number0, time0):
        self.correct = correct0
        self.number = number0
        self.time = time0

    def log(self, file):
        # log data to CSV, pass file object NOT filename
        pass
    
    def inform(self):
        global trials
        global trialsValid
        if self.correct:
            print(f"Correct in {self.time}")
        else:
            print(f"Incorrect - Trial not recorded")
        print(f"{trialsValid}/100 \t ({trials})")

def countdown():
    print("3")
    time.sleep(1000)
    print("2")
    time.sleep(1000)
    print("1\n")
    time.sleep(1000)

def runTest():
    global trials
    global trialsValid
    number = Number()
    countdown()
    start_time = time.perf_counter()
    print(number)
    response = input()
    end_time = time.perf_counter()
    duration = end_time - start_time
    try:
        correct = (int(response) == number.num)
        trialsValid += 1
    except:
        correct = False
    trials += 1
    response = Response(correct, number, duration)