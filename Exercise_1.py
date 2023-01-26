# File: Exercise_1.py
# Author: Riina Hahko
# Description: Programming demo 

import random

def main():
    
    # 1.
    print("Hello")

    # 2.
    print("2, -5, 4, 7, 9, 11, 0, 445, -100, 4")

    print("abc, 34re5, word, qwerty, cat-doc, def, 4, #-!?bc, alkf, oooooo")
    
    # 3.
    list = [2, -5, 4, 7, 9, 11, 0, 445, -100, 4]
    list.sort()
    print(list)

    # 4.
    input_1 = int(input("Please give an integer: "))
    input_2 = int(input("Please give an integer: "))
    input_3 = int(input("Please give an integer: "))

    input_list = [input_1, input_2, input_3]

    neg_count = 0
    num = 0

    for num in input_list:

        if num < 0:
            neg_count += 1
    
    print("Number of negative integers: ", neg_count)

main()

def main():
    # 5.
    input_1 = int(input("Please give an integer: "))
    input_2 = int(input("Please give an integer: "))
    input_3 = int(input("Please give an integer: "))
    input_4 = int(input("Please give an integer: "))

    input_list = [input_1, input_2, input_3, input_4]

    even_count = 0
    num = 0
    
    for num in input_list:
        
        if num != 0 and num % 2 == 0:

            even_count += 1
        
    print("Number of even integers is: ", even_count)

main()

def main():

    # 6.
    input_1 = int(input("Please give an integer: "))
    input_2 = int(input("Please give an integer: "))
    input_3 = int(input("Please give an integer: "))
    input_4 = int(input("Please give an integer: "))
    input_5 = int(input("Please give an integer: "))
    
    input_list = [input_1, input_2, input_3, input_4, input_5]

    pos_count = 0
    num = 0

    for num in input_list:

        if num > 0 and num % 3 == 0: 

             pos_count = pos_count + num

    print("Sum of positive integers divisible by three is: ", pos_count)

main()

def main():

    # 7.
    user_input = int(input("Give maximum value: "))
    list = [num for num in range(user_input) if num > 0 and num % 3 == 0]
    print("Procession is: ", list)
    print("Number of terms is: ", len(list))
    print("Sum of terms is: ", sum(list))
    print("Sum of squared terms is: ", sum(i*i for i in list))
    
main()

def main():
    
    # 8.
    print()

main()

def main(): 

    # 9.
    def random_number():
        num = random.randint(1,6)
        return num
    
    print("Random number is: ", random_number())

main() 