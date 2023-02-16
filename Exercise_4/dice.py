
import random

class Dice:

    def __init__(self):
        self.side = 1

    def roll(self):
        self.side = random.randint(1,6)

    def get_side(self):
        return self.side
    
def main():
    my_dice = Dice()
    my_dice.roll()
    print(my_dice.get_side())

main()