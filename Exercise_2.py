# File: Exercise_2.py
# Author: Riina Hahko
# Description: Exercise2, Task 3



def main(): 

    # 3.
    
    while True:
        user_input = input("Exercise points: ")

        try:
            point = int(user_input)

            if point >= 0 and point <= 120:
                
                if point >= 60 and point < 71:
                    print("Your grade is: 1")

                elif point >= 71 and point < 83:
                    print("Your grade is: 2")

                elif point >= 83 and point < 95:
                    print("Your grade is: 3")

                elif point >= 96 and point < 107:
                    print("Your grade is: 4")

                elif point >= 107 and point <= 120:
                    print("Your grade is: 5")
                    
                elif point < 60:
                    print("Your grade is: 0") 
                break

            else:
                print("Error: exercise points cannot be < 0 or > 120.")
        
        except ValueError:
            print("Error: exercise points cannot be < 0 or > 120.")
        

main()

def main(): 

    #5
    student_name = []
    current_student = ""
    student_amount = 0
    student_grade = []
    current_grade = 0
    grade_total = 0

    while True:
        current_student = input("Give students first name: ")
        student_name.append(current_student)
        student_amount += 1

        while True:
            try: 
                current_grade = int(input("Give students grade: "))
                if current_grade >= 0 and current_grade <= 5:
                    student_grade.append(current_grade)
                    grade_total += current_grade
                    break

                else:
                    print("Error; enter a grade between 0-5")
            except ValueError:
                print("Error; enter a grade between 0-5")
    
        user_choice = ""
        
        while user_choice != "Y" or user_choice != "y" or user_choice != "N" or user_choice != "n":
            user_choice = input("Do you want to add more students? Y/N: ")

            if user_choice == "Y" or user_choice =="y":
                break
            elif user_choice == "N" or user_choice == "n":
                break
        
        if user_choice == "Y" or user_choice == "y":
            continue
        elif user_choice == "N" or user_choice == "n":
            break

    print("The average grade from all students is: ", grade_total/student_amount)

main()

import random 
import time 

class Coin:
        def __init__(self):
            self.sideup = "Heads"

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

        def get_sideup(self):
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
                    print("The portal swallows you up into complete daekness...")
                    time.sleep(2)
                    print("You are trapped. Game over!")
                    break
def main():


    my_coin = Coin()
    my_player = Player()
    print("The state of the coin is this: ")
    print(my_coin.get_sideup())
    while True:
                my_player.guess()
                print("Let's toss the coin")
                my_coin.toss()
                print(my_coin.get_sideup())
                if (my_player.player_guess == my_coin.random_int):
                    print("You win! Current score: ")
                    print(my_player.correct_guess)
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