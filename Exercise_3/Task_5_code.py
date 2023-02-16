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
        print("")

    def pickColor(self):
        self.colorList = ["Red", "Blue", "Yellow", "Orange"]
        self.selector = random.randint(0,3)
        self.color = self.colorList[self.selector]
    
    def getSideAndColor(self):
        return "Number: " + str(self.diceSide) + "Color: " + self.color
    
    def iForgot(self):
        return "I picked the dice up and forgot the numbers..."
        
    def iRemember(self):
        printVar = "I remember them again ! The numbers were: " + str(self.diceSide)
        
def main():

    Dice1 = Dice()
    Dice2 = Dice()
    Dice3 = Dice()
    round = 1 
    maxround = 3 
    PlayerScore = [0,0,0]
    Players = ["Player 1", "Player 2", "Player 3"]
    tieMaker = ["",""]
    print("Dice rolling game")
    print("Let's roll the dice!")
    
    while True:
        print("Roud ", round, "/",maxround)
        print("")
        print("Player 1: "),Dice1.rollTheDice()
        PlayerScore[0] += Dice1.diceSide
        print("Player 2: "),Dice2.rollTheDice()
        PlayerScore[1] += Dice2.diceSide
        print("Player 3: "),Dice3.rollTheDice()
        PlayerScore[2] += Dice3.diceSide
        print("")

        if (round == maxround):
            break
        else:
            round += 1
            continue

    print("The scores are as follows: ")
    counter = 1

    for i in PlayerScore:
        print("Player",counter,":",1)
        counter += 1

    winner = max(PlayerScore)

    if PlayerScore.count(winner) == 1:
        if winner ==PlayerScore[0]:
            print("Player 1 wins with a score of ",winner)
        
        elif winner == PlayerScore[1]:
            print("Player 2 wins with a score of ",winner)

        else:
            print("Player 3 wins with a score of ",winner)

    elif PlayerScore.count(winner) == 3:
        print("All 3 players are tied, let's try again!")
        main()

    else:
        counter = 0
        for x in range(0,3):
            if(PlayerScore[x] == winner):
                tieMaker[counter] += Players[x]
                counter += 1
                if (tieMaker[1] != ""):
                    break

                else:
                    continue
        print("There is a tie between ", tieMaker[0], " and", tieMaker[1])
        time.sleep(1)
        print("Let's throw a coin to decide the winner!")
        time.sleep(1)
        print("If tails, first player wins. If heads, second player wins.")
        time.sleep(1)
        coin_toss = random.randint(0,1)
        
        if(coin_toss == 0):
            coin_side = "Tails"
            print("The coin landed on: ",coin_side)
            time.sleep(2)
            print(tieMaker[0], "Wins!")
        
        elif(coin_toss == 1):
            coin_side = "Heads"
            print("The coin landed on: ",coin_side)
            time.sleep(2)
            print(tieMaker[1], " Wins!")

main()


