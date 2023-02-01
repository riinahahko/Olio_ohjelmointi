# File: Exercise_2.py
# Author: Riina Hahko
# Description: Programming demo



def main(): 

    while True:
        user_input = input("Exercise points: ")

        try:
            point = int(user_input)

            if point >= 0 and point <= 120:
                
                if point >= 50 and point <= 64:
                    print("Your grade is: 1")

                elif point >= 65 and point <= 78:
                    print("Your grade is: 2")

                elif point >= 79 and point <= 92:
                    print("Your grade is: 3")

                elif point >= 93 and point <= 106:
                    print("Your grade is: 4")

                elif point >= 107 and point <= 120:
                    print("Your grade is: 5")
                    
                elif point < 50:
                    print("Your grade is: No grade") 
                break

            else:
                print("Error: exercise points cannot be <0 or >120.")
        
        except ValueError:
            print("Error: exercise points cannot be <0 or >120.")
        

main()
