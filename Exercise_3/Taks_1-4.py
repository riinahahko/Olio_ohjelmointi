# File: Exercise_3.py
# Author: Riina Hahko
# Description: Programming demo

# Task 1;
# Abstraction - packages of indidual parts of the code.
# Accessor method - method used to access the state of the object i.e, the data hidden in the object can be accessed from this method.
# Mutator method - method used to mutate/modify the state of an object i.e, alters the hidden value of the data variable.
# Public method can be invoked from anywhere, no restrictions on its use.
# Private method is internat to the implematation of a class and can only be called by other instance methods of the class.
# __str__ method represents the class objects as a string.

# Task 2;

import random 
import time 

class Coin:
        def __init__(self):
            self.sideup = "Heads"
            self.currency = ""

        def setCurrency(self):
            self.possibleCurrencies = ["Euro", "Pound", "Dollar", "Swedish krona", "Yen"]
            self.selector = random.randint(0,len(self.possibleCurrencies))
            self.currency = self.possibleCurrencies[self.selector]
            print(self.currency)

        def toss(self):
            self.random_int = random.randint(0,4)
            if self.random_int == 0:
                self.sideup = "Heads"
            elif self.random_int == 1:
                self.sideup = "Tails"
            elif self.random_int == 2:
                self.sideup = "Upright"
            elif self.random_int == 3:
                self.sideup = "Ground"
            elif self.random_int == 4:
                self.sideup = "Wormhole"

        def __get_sideup(self):
            return self.sideup

        def wormhole_toss(self):
            self.coin_landing = random.randint(0,2)
            
            if self.coin_landing == 0:
                self.sideup = "Heads"
            if self.coin_landing == 1:
                self.sideup = "Heads"
            if self.coin_landing == 2:
                self.sideup = "Side"
        
class Player(Coin):

        def __init__(self):
            self.player_score = 0

        def guess (self):
            self.player_guess = int(input("Guess which way the coin falls: Press 1 for Heads, 2 for Tails: "))
            print("You guessed: ")
            print(self.player_guess)
        
        def correct_guess(self):
            self.player_score += 1
            return self.player_score
        
        def wrong_guess(self):
            self.player_score += 0
            return self.player_score
        
        def wormhole(self):
            while True:
                print("In this wormhole, the laws of physics are bent.")
                print("This is the deciding moment, guess the way the coin lands. Press 1 for Heads, 2 for Tails, 3 for the coin landing on the side!")
                self.guess()
                self.wormhole_toss()
                
                if (self.player_guess == self.coin_landing):
                    print("The coin starts glowing... you guessed correctly...")
                    time.sleep(2)
                    print("The wormhole transports you to an unfamiliar place...")
                    time.sleep(2)
                    print("You won! Game over!")
                    break

                elif (self.player_guess != self.coin_landing):
                    print("The coin starts warping into a portal...")
                    time.sleep(2)
                    print("The portal swallows you up into complete darkness...")
                    time.sleep(2)
                    print("You are trapped. Game over!")
                    break
def main():


    my_coin = Coin()
    my_player = Player()
    my_coin.setCurrency()
    print("The state of the coin is this: ")
    print(my_coin._Coin__get_sideup())

    while True:
                my_player.guess()
                print("Let's toss the coin")
                my_coin.toss()
                print(my_coin._Coin__get_sideup())
                if (my_player.player_guess == my_coin.random_int):
                    print("You win! Current score: ")
                    print(my_player.correct_guess())
                    continue

                elif (my_coin.sideup == "Upright"): 
                    print("The coin landed on its side, try again!")
                    continue

                elif(my_coin.sideup == "Ground"):
                    print("The coin dropped to the ground and into a rabbit hole! Try again!")
                    continue

                elif (my_coin.sideup == "Wormhole"):
                    print("The coin defied gravity and got lost in a wormhole! Watch out!")
                    my_player.wormhole()
                    break

                else:
                    print("You lose! Current score: ")
                    print(my_player.wrong_guess())
                    continue

main()

main()