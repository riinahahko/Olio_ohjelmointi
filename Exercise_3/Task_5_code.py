# File: Task_5.py
# Author: Riina Hahko 
# Description: Task 5 coding 

import random 
import time 

class Dice:
    def __init__(self):
        self.diceSide = 1 
        self.color = "placeholder"
    
    def rollTheDice(self):
        print("Let's roll the dice")
        self.diceSide = random.randint(1,6)
        print("You rolled :", self.diceSide)

    def pickColor(self):
        self.colorList = ["Red", "Blue", "Yellow", "Orange"]
        self.selector = random.randint(0,3)
        self.color = self.colorList[self.selector]
    
    def getSideAndColor(self):
        return self.diceSide, self.color
    
    def iForgot(self):
        return "I picked the dice up and forgot the numbers..."
        
    def iRemember(self):
        printVar = "I remember them again ! The numbers were: " + str(self.diceSide)
        return printVar
    
def main():

    Dice1 = Dice()
    Dice1.rollTheDice()

    randomInt = random.randint(0,1)

    if (randomInt == 1):
        Dice1.iForgot()
        print(Dice1.iForgot())
        time.sleep(1)

        randomInt = random.randint(0,1)
        if (randomInt == 1):
            print(Dice1.iRemember())

        else:
            print(Dice1.iForgot())
            return 0
    
    Dice1.pickColor()
    Dice1.getSideAndColor()

main()