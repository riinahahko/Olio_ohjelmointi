
import random 

def main():

    users_pick = input("Give your choice (R, P, S): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computers_pick = random.choice(possible_actions)
    print("Computer's choice is", computers_pick)
    

    if users_pick == computers_pick:
        print("It's a tie!")

    elif users_pick == "R":

        if computers_pick == "Scissors":
            print("Rock crushes Scissors.")

        else:
            print("Paper covers Rock.")

    elif users_pick == "P":

        if computers_pick == "Rock":
            print("Paper covers Rock.")

        else:
            print("Scissors cuts Paper.")

    elif users_pick == "S":

        if computers_pick == "Paper":
            print("Scissors cuts paper.")

        else: 
            print("Rock crushes Scissors.")

main()