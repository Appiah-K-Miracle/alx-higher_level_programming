#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = abs(number) % 10
if number < 0:
    lastNumber = -(lastNumber)
theWord = "Last digit of ", number ,"is ",lastNumber
if lastNumber > 5:
    print(theWord," and is greater than 5")
elif lastNumber == 0:
    print(theWord," and is 0")
elif lastNumber < 6:
    print(theWord, " and is less than 6 and not 0")
