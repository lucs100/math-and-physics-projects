import random
from time import sleep, perf_counter_ns
import csv

# Code for MTE 201 Lab 1
# Lucas Di Pietro, 2022

KnownAreaCodes = ["519", "905", "289", "365"]

trials = 0
trialsValid = 0
TARGET_TRIALS_COMPLETE = 100

default_fp = "programs/phone-number-typing/times.csv"

class Number:
    def __init__(self):
        ac0 = random.choice(KnownAreaCodes)
        finalNum = str(ac0)
        finalStr = str(ac0) + '-'
        for i in range(1+3, 11):
            n = str(random.randint(0, 9))
            finalNum += n
            finalStr += n
            if i == 6:
                finalStr += '-'
        self.ac = ac0
        self.num = int(finalNum)
        self.string = finalStr

    def __repr__(self):
        return self.string

class Response:
    def __init__(self, correct0, number0, time0, trials):
        self.correct = correct0
        self.number = number0
        self.time = time0
        self.idnum = trials

        if self.correct:
            print(f"Correct in {self.time}s")
        else:
            print(f"Incorrect - Trial not recorded")
        print(f"{trialsValid}/100 \t ({trials} total)")
        input("Press enter...")
    
    def export(self):
        return [self.idnum, self.number.ac, self.number.num, self.time]

    def log(self, file=default_fp):
        csvfile = open(file, 'a', newline = '')
        logWriter = csv.writer(csvfile)
        logWriter.writerow(self.export())
        csvfile.close()
        # update with a csv

def countdown():
    print("3")
    sleep(.5)
    print("2")
    sleep(.5)
    print("1\n")
    sleep(.5)

def runTest():
    global trials
    global trialsValid

    while trialsValid < TARGET_TRIALS_COMPLETE:
        number = Number()
        countdown()
        start_time = perf_counter_ns()
        print(number)
        print("\n")
        response = input()
        end_time = perf_counter_ns() 
        duration = (end_time - start_time)/(10**9)
        try:
            correct = (int(response) == number.num)
            if correct:
                trialsValid += 1
        except:
            correct = False
        trials += 1
        response = Response(correct, number, duration, trials)
        if correct:
            response.log()

runTest()