# File: Exercise_2.py
# Author: Riina Hahko
# Description: Exercise2, Task 3



def main(): 

    while True:
        user_input = input("Exercise points: ")

        try:
            point = int(user_input)

            if point >= 0 and point <= 120:
                
                if point >= 60 and point <= 71:
                    print("Your grade is: 1")

                elif point >= 72 and point <= 83:
                    print("Your grade is: 2")

                elif point >= 84 and point <= 95:
                    print("Your grade is: 3")

                elif point >= 96 and point <= 107:
                    print("Your grade is: 4")

                elif point >= 108 and point <= 120:
                    print("Your grade is: 5")
                    
                elif point < 60:
                    print("Your grade is: 0") 
                break

            else:
                print("Error: exercise points cannot be < 0 or > 120.")
        
        except ValueError:
            print("Error: exercise points cannot be < 0 or > 120.")
        

main()
